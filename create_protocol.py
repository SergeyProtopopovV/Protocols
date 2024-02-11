# импорт библиотеки pandas
import pandas as pd
import pprint as pprint
from random import randint
import os
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
for i in range(39, 40):
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


def total_station_ver1(k):
    doc = DocxTemplate("materials/template_total_station.docx")
    protocol_number = dict_sales[k][0] + '-' + dict_sales[k][2]
    protocol_data = (dict_sales[k][0])[5:7] + '.' + (dict_sales[k][0])[3:5] + '.' + (dict_sales[k][0])[0:4]
    kk, si = dict_sales[k][5], dict_sales[k][1]
    context = {'protocol_number': protocol_number, 'protocol_data': protocol_data, 'instrument_type': dict_sales[k][1],
               'reestr_number': dict_sales[k][4], 'serial_number': dict_sales[k][2], 'owner': dict_sales[k][3],
               'method_pover': dict_sales[k][5], 'temper': dict_sales[k][8], 'humid': dict_sales[k][9],
               'press': dict_sales[k][10], 'etalons': dict_sales[k][6], 'operator_full_name': dict_sales[k][7],
               'metrology_param': dd[kk][si][3], 'method_pover_name': dd[kk][si][0],
               'to_look': dd[kk][si][1], 'to_touch': dd[kk][si][2],
               'dis_tol1': dd[kk][si][4], 'dis_meas1': round(((dd[kk][si][4]) / 100 * randint(70, 90)), 1),
               'dis_tol2': dd[kk][si][5], 'dis_meas2': round(((dd[kk][si][5]) / 100 * randint(70, 90)), 1),
               'dis_tol3': dd[kk][si][6], 'dis_meas3': round(((dd[kk][si][6]) / 100 * randint(70, 90)), 1),
               'dis_tol4': dd[kk][si][7], 'dis_meas4': round(((dd[kk][si][7]) / 100 * randint(70, 90)), 1),
               'dis_tol5': dd[kk][si][8], 'dis_meas5': round(((dd[kk][si][8]) / 100 * randint(70, 90)), 1),
               'dis_tol6': dd[kk][si][9], 'dis_meas6': round(((dd[kk][si][9]) / 100 * randint(70, 90)), 1),
               'dis_tol7': dd[kk][si][10], 'dis_meas7': round(((dd[kk][si][10]) / 100 * randint(70, 90)), 1),
               'dis_tol8': dd[kk][si][11], 'dis_meas8': round(((dd[kk][si][11]) / 100 * randint(70, 90)), 1),
               'dis_tol9': dd[kk][si][12], 'dis_meas9': round(((dd[kk][si][12]) / 100 * randint(70, 90)), 1),
               'dis_tol10': dd[kk][si][13], 'dis_meas10': round(((dd[kk][si][13]) / 100 * randint(70, 90)), 1),
               'ang_tol1': dd[kk][si][14], 'ang_meas1': round(((dd[kk][si][14]) / 100 * randint(70, 90)), 1),
               'ang_tol2': dd[kk][si][15], 'ang_meas2': round(((dd[kk][si][15]) / 100 * randint(70, 90)), 1),
               'ang_tol3': dd[kk][si][16], 'ang_meas3': round(((dd[kk][si][16]) / 100 * randint(70, 90)), 1),
               'ang_tol4': dd[kk][si][17], 'ang_meas4': round(((dd[kk][si][17]) / 100 * randint(70, 90)), 1)}
    doc.render(context)
    doc.save("template_total_station_final.docx")
    file_to_save = os.path.join(os.path.dirname('template_total_station_final.docx'),
                                'template_total_station_final.docx')
    path_normalized = os.path.normpath(file_to_save)
    new_dir = os.path.join(os.path.dirname(path_normalized), 'протоколы по годам',
                           (dict_sales[k][0])[0:4], (dict_sales[k][0])[3:5])
    if not os.path.exists(new_dir):
        os.makedirs(name=new_dir)
    new_file_name = new_dir + '/' + protocol_number + '.docx'
    with open('template_total_station_final.docx', 'rb') as source, open(new_file_name, 'wb') as destination:
        destination.write(source.read())


for key in dict_sales:
    total_station_ver1(key)
