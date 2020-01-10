with open('/Users/suntian/codes/DailyPractice/情感分类/code.tsv', 'w+', encoding="utf8")as t:
    with open("/Users/suntian/codes/DailyPractice/情感分类/code.txt", 'r', encoding='utf8')as f:
        for line in f.readlines():
            line_list = line.strip('\n').split()
            tsv_list = '\t'.join(line_list)
            t.write(tsv_list+'\n')