import xlrd
import os
filename="calcu_result283.xlsx"
filepath=os.path.join(os.getcwd(),filename)
excel_data=xlrd.open_workbook(filepath)
sheet=excel_data.sheet_by_index(0)
sheet_rows=sheet.nrows
print("Excel的行数：",sheet_rows)
sheet_cols=sheet.ncols
print("Excle的列数：",sheet_cols)
first_row=sheet.row_values(0)
print(first_row)
def Read_data():
    x=[]
    for i in range(sheet_cols):
        if first_row[i] == 'payment_base':
            print("该字段的位置是：",i)
            #payment_base_data=sheet.col_values(i,1)
            x.append(i)
            continue
        elif first_row[i] == 'hist_payment_base_projection':
            print("该字段的位置是：",i)
            #hist_payment_base_projection_data = sheet.col_values(i,1)
            x.append(i)
        else:
            pass
    return x
a=Read_data()
for i in range(len(a)):
    print(sheet.col_values(a[i],1))





















