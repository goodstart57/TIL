import win32com.client

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True
wb = excel.Workbooks.Open('C:\\Users\\folwo\\Desktop\\test.xlsx')
ws = wb.ActiveSheet

ws.Cells(1, 1).Value = "hello world"
ws.Cells(1, 2).Value = "hello world2"
wb.SaveAs('c:\\Users\\folwo\\Desktop\\test.xlsx')
excel.Quit()