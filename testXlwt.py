import xlwt

Workbook = xlwt.workbook(encoding="utf-8")  #创建workbook对象
worksheet = Workbook.add_sheet('sheet1')    #创建工作表
worksheet.write(0,0,'hello') #写入数据，第一个参数表示“行”，第二个参数表示列，第三个表示内容
Workbook.save('student.xls')