from keras.layers import Embedding, SimpleRNN, Dropout, Dense
from keras.models import Sequential
from sklearn.model_selection import train_test_split
from keras.preprocessing.sequence import pad_sequences
from gensim.models import Word2Vec
import pandas as pd
import re
import logging

logging.basicConfig(filename='/root/tian/pytorch_project/情感分类/example.log',
                    filemode='w', level=logging.DEBUG)

# 读取数据
data = pd.read_csv(
    r"/root/tian/pytorch_project/情感分类/code.tsv", sep='\t')
data.dropna(axis=0, how='any', inplace=True)


def clean_review(raw_review):
    if raw_review is None:
        pass
    else:
        word_list = raw_review.split('/')
    return word_list


sentences = data.review.apply(clean_review)

embedding_vector_size = 256
w2v_model = Word2Vec(
    sentences=sentences,
    size=embedding_vector_size,
    min_count=3, window=5, workers=4)

# cal_len = pd.DataFrame()
# cal_len['review_lenght'] = list(map(len, sentences))
# print("中位数：", cal_len['review_lenght'].median())
# print("均值数：", cal_len['review_lenght'].mean())
# del cal_len

# 取得所有单词
vocab_list = list(w2v_model.wv.vocab.keys())
# 每个词语对应的索引
word_index = {word: index for index, word in enumerate(vocab_list)}


def get_index(sentence):
    global word_index
    sequence = []
    for word in sentence:
        try:
            sequence.append(word_index[word])
        except KeyError:
            pass
    return sequence


X_data = list(map(get_index, sentences))


# 截长补短
# max_len 根据中位数和平均值得来的
maxlen = 20
X_pad = pad_sequences(X_data, maxlen=maxlen)
# 取得标签
Y = data.sentiment.values
# 划分数据集
X_train, X_test, Y_train, Y_test = train_test_split(
    X_pad,
    Y,
    test_size=0.2,
    random_state=42)

# 让 Keras 的 Embedding 层使用训练好的Word2Vec权重
embedding_matrix = w2v_model.wv.vectors

model = Sequential()
model.add(Embedding(
    input_dim=embedding_matrix.shape[0],
    output_dim=embedding_matrix.shape[1],
    input_length=maxlen,
    weights=[embedding_matrix],
    trainable=False))
model.add(SimpleRNN(128, recurrent_dropout=0.1))
model.add(Dropout(0.25))
model.add(Dense(128, activation='sigmoid'))
model.add(Dropout(0.3))
model.add(Dense(1, activation='sigmoid'))

model.compile(
    loss="binary_crossentropy",
    optimizer='adam',
    metrics=['accuracy']
)

history = model.fit(
    x=X_train,
    y=Y_train,
    validation_data=(X_test, Y_test),
    batch_size=50,
    epochs=8
)

# evaluate the model
loss, acc = model.evaluate(X_test, Y_test, verbose=0)
print('Test loss:', loss)
print('Test accuracy:', acc)
