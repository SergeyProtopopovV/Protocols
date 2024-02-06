# импорт библиотеки pandas
import pandas as pd
import pprint
from docxtpl import DocxTemplate

from dopuska_total_station import dict_dopuska as dd

# Загружаем ваш файл в переменную `file` / вместо 'example' укажите название свого файла из текущей директории
file = 'materials/POV-ГСИ.XLS'
# Загружаем spreadsheet в объект pandas
xl = pd.ExcelFile(file)
# # Печатаем название листов в данном файле
# print(xl.sheet_names)
# Загрузить лист в DataFrame по его имени: df1
df1 = xl.parse('Продажа')

dict_sales = {}
list_sales = []

count = 0
for i in range(39, 41):
    try:
        item_data = str(df1.loc[i][13].year) + str(df1.loc[i][13].month) + str(df1.loc[i][13].day)
        instrument = str(df1.loc[i][0]) + " " + str(df1.loc[i][1])
        dict_sales[i] = (item_data, instrument, df1.loc[i][2], df1.loc[i][10], df1.loc[i][22], df1.loc[i][23],
                         df1.loc[i][24], df1.loc[i][30], df1.loc[i][31], df1.loc[i][32], df1.loc[i][33])
        list_sales.append(df1.loc[i][23])
    except Exception as exc:
        count += 1
        print(f'Ошибка {exc} в строке {i}')

print(f'пустых строк - {count}')
pprint.pprint(dict_sales)
list_sales_separate = set(list_sales)
pprint.pprint(list_sales_separate)
print(len(list_sales_separate))

doc = DocxTemplate("materials/template_total_station.docx")
protocol_number = dict_sales[39][0] + '-' + dict_sales[39][2]
protocol_data = (dict_sales[39][0])[5:7] + '.' + (dict_sales[39][0])[3:5] + '.' + (dict_sales[39][0])[0:4]
context = {'protocol_number': protocol_number, 'protocol_data': protocol_data, 'instrument_type': dict_sales[39][1],
           'reestr_number': dict_sales[39][4], 'serial_number': dict_sales[39][2], 'owner': dict_sales[39][3],
           'method_pover': dict_sales[39][5], 'temper': dict_sales[39][8], 'humid': dict_sales[39][9],
           'press': dict_sales[39][10], 'etalons': dict_sales[39][6], 'operator_full_name': dict_sales[39][7],
           'metrology_param': dd[dict_sales[39][4]][dict_sales[39][1]][3],
           'method_pover_name': dd[dict_sales[39][4]][dict_sales[39][1]][0],
           'to_look': dd[dict_sales[39][4]][dict_sales[39][1]][1],
           'to_touch': dd[dict_sales[39][4]][dict_sales[39][1]][2]}
doc.render(context)
doc.save("template_total_station_final.docx")
