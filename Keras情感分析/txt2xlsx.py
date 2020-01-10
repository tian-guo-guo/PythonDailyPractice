import xlwt
import codecs


def Txt_to_Excel(inputTxt, sheetName, start_row, start_col, outputExcel):
    fr = codecs.open(inputTxt, 'r')
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet(sheetName)

    line_number = 0  # 记录有多少行，相当于写入excel时的i，
    row_excel = start_row
    try:
        for line in fr:
            line_number += 1
            row_excel += 1
            line = line.strip()
            line = line.split(' ')
            len_line = len(line)  # list中每一行有多少个数，相当于写入excel中的j
            col_excel = start_col
            for j in range(len_line):
                # print(line[j])
                ws.write(row_excel, col_excel, line[j])
                col_excel += 1
                wb.save(outputExcel)
    except:
        print('')


if __name__ == '__main__':
    sheetName = 'Sheet1'  # 需要写入excel中的Sheet2中，可以自己设定
    start_row = 1  # 从第7行开始写
    start_col = 2  # 从第3列开始写
    inputfile = '/Users/suntian/codes/DailyPractice/情感分类/all_data.txt'  # 输入文件
    outputExcel = '/Users/suntian/codes/DailyPractice/情感分类/data.xls'  # 输出excel文件
    Txt_to_Excel(inputfile, sheetName, start_row, start_col, outputExcel)
