import pandas as pd
import pprint as pprint
from random import randint
import os
import time
from docxtpl import DocxTemplate
from dopuska_total_station import dict_dopuska_total_station as d_t_s
from dopuska_measuring_tape_staff import dict_dopuska_measuring_tape_staff as d_m_t_s
from dopuska_optical_level import dict_dopuska_optical_level as d_o_l
import change_instruments as c_i

# Загружаем ваш файл в переменную `file` / вместо 'example' укажите название своего файла из текущей директории
file = 'materials/POV-ГСИ.XLS'
# Загружаем spreadsheet в объект pandas
xl = pd.ExcelFile(file)
# # Печатаем название листов в данном файле
# print(xl.sheet_names)
# Загрузить лист в DataFrame по его имени: df1
df1 = xl.parse('Продажа')

dict_sales = {}
list_sales = []

count_lines = 0
count_empty_lines = 0
count_records_in_dict = 0
count_files_created = 0

# for i in range(26200, 26250):
for i in range(9863, 24410):
    count_lines += 1
    try:
        instrument = str(df1.loc[i][0]) + " " + str(df1.loc[i][1])
        instrument = " ".join(instrument.split())
        dict_sales[i] = (df1.loc[i][13].date(), instrument, df1.loc[i][2], df1.loc[i][10], df1.loc[i][22],
                         df1.loc[i][23], df1.loc[i][24], df1.loc[i][30], df1.loc[i][31], df1.loc[i][32], df1.loc[i][33])
        list_sales.append(df1.loc[i][23])
        count_records_in_dict += 1
    except Exception as exc:
        count_empty_lines += 1
        print(f'Ошибка {exc} пустая строка {i + 2}')

# pprint.pprint(dict_sales[20168])
# list_sales_separate = set(list_sales)
# pprint.pprint(list_sales_separate)


def total_station_ver1(k):
    doc = DocxTemplate("materials/template_total_station_ver1.docx")
    protocol_number = str(dict_sales[k][0]) + '-' + str(dict_sales[k][2])
    protocol_name = str(dict_sales[k][0]) + '-' + dict_sales[k][1] + '-' + str(dict_sales[k][2])
    protocol_data = dict_sales[k][0]
    kk, si = dict_sales[k][5], dict_sales[k][1]
    context = {'protocol_number': protocol_number, 'protocol_data': protocol_data, 'instrument_type': dict_sales[k][1],
               'reestr_number': dict_sales[k][4], 'serial_number': dict_sales[k][2], 'owner': dict_sales[k][3],
               'method_pover': dict_sales[k][5], 'temper': dict_sales[k][8], 'humid': dict_sales[k][9],
               'press': dict_sales[k][10], 'etalons': dict_sales[k][6], 'operator_full_name': dict_sales[k][7],
               'metrology_param': d_t_s[kk][si][3], 'method_pover_name': d_t_s[kk][si][0],
               'to_look': d_t_s[kk][si][1], 'to_touch': d_t_s[kk][si][2],
               'dis_tol1': d_t_s[kk][si][4], 'dis_meas1': round(((d_t_s[kk][si][4]) / 100 * randint(70, 90)), 1),
               'dis_tol2': d_t_s[kk][si][5], 'dis_meas2': round(((d_t_s[kk][si][5]) / 100 * randint(70, 90)), 1),
               'dis_tol3': d_t_s[kk][si][6], 'dis_meas3': round(((d_t_s[kk][si][6]) / 100 * randint(70, 90)), 1),
               'dis_tol4': d_t_s[kk][si][7], 'dis_meas4': round(((d_t_s[kk][si][7]) / 100 * randint(70, 90)), 1),
               'dis_tol5': d_t_s[kk][si][8], 'dis_meas5': round(((d_t_s[kk][si][8]) / 100 * randint(70, 90)), 1),
               'dis_tol6': d_t_s[kk][si][9], 'dis_meas6': round(((d_t_s[kk][si][9]) / 100 * randint(70, 90)), 1),
               'dis_tol7': d_t_s[kk][si][10], 'dis_meas7': round(((d_t_s[kk][si][10]) / 100 * randint(70, 90)), 1),
               'dis_tol8': d_t_s[kk][si][11], 'dis_meas8': round(((d_t_s[kk][si][11]) / 100 * randint(70, 90)), 1),
               'dis_tol9': d_t_s[kk][si][12], 'dis_meas9': round(((d_t_s[kk][si][12]) / 100 * randint(70, 90)), 1),
               'dis_tol10': d_t_s[kk][si][13], 'dis_meas10': round(((d_t_s[kk][si][13]) / 100 * randint(70, 90)), 1),
               'ang_tol1': d_t_s[kk][si][14], 'ang_meas1': round(((d_t_s[kk][si][14]) / 100 * randint(70, 90)), 1),
               'ang_tol2': d_t_s[kk][si][15], 'ang_meas2': round(((d_t_s[kk][si][15]) / 100 * randint(70, 90)), 1),
               'ang_tol3': d_t_s[kk][si][16], 'ang_meas3': round(((d_t_s[kk][si][16]) / 100 * randint(70, 90)), 1),
               'ang_tol4': d_t_s[kk][si][17], 'ang_meas4': round(((d_t_s[kk][si][17]) / 100 * randint(70, 90)), 1)}
    doc.render(context)
    doc.save("template_total_station_ver1_final.docx")
    file_to_save = os.path.join(os.path.dirname('template_total_station_ver1_final.docx'),
                                'template_total_station_ver1_final.docx')
    path_normalized = os.path.normpath(file_to_save)
    new_dir = os.path.join(os.path.dirname(path_normalized), 'протоколы по годам',
                           str(dict_sales[k][0].year), f'{dict_sales[k][0].month:02d}')
    if not os.path.exists(new_dir):
        os.makedirs(name=new_dir)
    new_file_name = new_dir + '/' + protocol_name + '.docx'
    with open('template_total_station_ver1_final.docx', 'rb') as source, open(new_file_name, 'wb') as destination:
        destination.write(source.read())


def measuring_tape(k):
    doc = DocxTemplate("materials/template_measuring_tape.docx")
    protocol_number = str(dict_sales[k][0]) + '-' + str(dict_sales[k][2])
    protocol_name = str(dict_sales[k][0]) + '-' + dict_sales[k][1].replace('/', '_') + '-' + str(dict_sales[k][2])
    protocol_data = dict_sales[k][0]
    kk, si = dict_sales[k][5], dict_sales[k][1]
    context = {'protocol_number': protocol_number, 'protocol_data': protocol_data, 'instrument_type': dict_sales[k][1],
               'reestr_number': dict_sales[k][4], 'serial_number': dict_sales[k][2], 'owner': dict_sales[k][3],
               'method_pover': dict_sales[k][5], 'temper': dict_sales[k][8], 'humid': dict_sales[k][9],
               'press': dict_sales[k][10], 'etalons': dict_sales[k][6], 'operator_full_name': dict_sales[k][7],
               'metrology_param': d_m_t_s[kk][si][3], 'method_pover_name': d_m_t_s[kk][si][0],
               'to_look': d_m_t_s[kk][si][1], 'to_touch': d_m_t_s[kk][si][2],
               'diap1': d_m_t_s[kk][si][4], 'diap_tol1': d_m_t_s[kk][si][5],
               'diap_meas1': round(((d_m_t_s[kk][si][5]) / 100 * randint(70, 90)), 1),
               'diap2': d_m_t_s[kk][si][6], 'diap_tol2': d_m_t_s[kk][si][7],
               'diap_meas2': round(((d_m_t_s[kk][si][7]) / 100 * randint(70, 90)), 1),
               'diap3': d_m_t_s[kk][si][8], 'diap_tol3': d_m_t_s[kk][si][9],
               'diap_meas3': round(((d_m_t_s[kk][si][9]) / 100 * randint(70, 90)), 1),
               'diap4': d_m_t_s[kk][si][10], 'diap_tol4': d_m_t_s[kk][si][11],
               'diap_meas4': round(((d_m_t_s[kk][si][11]) / 100 * randint(70, 90)), 1),
               'diap5': d_m_t_s[kk][si][12], 'diap_tol5': d_m_t_s[kk][si][13],
               'diap_meas5': round(((d_m_t_s[kk][si][13]) / 100 * randint(70, 90)), 1),
               'diap6': d_m_t_s[kk][si][14], 'diap_tol6': d_m_t_s[kk][si][15],
               'diap_meas6': round(((d_m_t_s[kk][si][15]) / 100 * randint(70, 90)), 1),
               'diap7': d_m_t_s[kk][si][16], 'diap_tol7': d_m_t_s[kk][si][17],
               'diap_meas7': round(((d_m_t_s[kk][si][17]) / 100 * randint(70, 90)), 1),
               'diap8': d_m_t_s[kk][si][18], 'diap_tol8': d_m_t_s[kk][si][19],
               'diap_meas8': round(((d_m_t_s[kk][si][19]) / 100 * randint(70, 90)), 1),
               'diap9': d_m_t_s[kk][si][20], 'diap_tol9': d_m_t_s[kk][si][21],
               'diap_meas9': round(((d_m_t_s[kk][si][21]) / 100 * randint(70, 90)), 1),
               'diap10': d_m_t_s[kk][si][22], 'diap_tol10': d_m_t_s[kk][si][23],
               'diap_meas10': round(((d_m_t_s[kk][si][23]) / 100 * randint(70, 90)), 1),
               }
    doc.render(context)
    doc.save("template_measuring_tape_final.docx")
    file_to_save = os.path.join(os.path.dirname('template_measuring_tape_final.docx'),
                                'template_measuring_tape_final.docx')
    path_normalized = os.path.normpath(file_to_save)
    new_dir = os.path.join(os.path.dirname(path_normalized), 'протоколы по годам',
                           str(dict_sales[k][0].year), f'{dict_sales[k][0].month:02d}')
    if not os.path.exists(new_dir):
        os.makedirs(name=new_dir)
    new_file_name = new_dir + '/' + protocol_name + '.docx'
    with open('template_measuring_tape_final.docx', 'rb') as source, open(new_file_name, 'wb') as destination:
        destination.write(source.read())


def staff(k):
    doc = DocxTemplate("materials/template_staff.docx")
    protocol_number = str(dict_sales[k][0]) + '-' + str(dict_sales[k][2])
    protocol_name = str(dict_sales[k][0]) + '-' + dict_sales[k][1] + '-' + str(dict_sales[k][2])
    protocol_data = dict_sales[k][0]
    kk, si = dict_sales[k][5], dict_sales[k][1]
    context = {'protocol_number': protocol_number, 'protocol_data': protocol_data, 'instrument_type': dict_sales[k][1],
               'reestr_number': dict_sales[k][4], 'serial_number': dict_sales[k][2], 'owner': dict_sales[k][3],
               'method_pover': dict_sales[k][5], 'temper': dict_sales[k][8], 'humid': dict_sales[k][9],
               'press': dict_sales[k][10], 'etalons': dict_sales[k][6], 'operator_full_name': dict_sales[k][7],
               'metrology_param': d_m_t_s[kk][si][3], 'method_pover_name': d_m_t_s[kk][si][0],
               'to_look': d_m_t_s[kk][si][1], 'to_touch': d_m_t_s[kk][si][2],
               'staff_tol1': d_m_t_s[kk][si][4],
               'staff_meas1': round(((d_m_t_s[kk][si][4]) / 100 * randint(70, 90)), 1),
               'staff_tol2': d_m_t_s[kk][si][5],
               'staff_meas2': round(((d_m_t_s[kk][si][5]) / 100 * randint(70, 90)), 1),
               'staff_tol3': d_m_t_s[kk][si][6],
               'staff_meas3': round(((d_m_t_s[kk][si][6]) / 100 * randint(70, 90)), 1),
               'staff_tol4': d_m_t_s[kk][si][7],
               'staff_meas4': round(((d_m_t_s[kk][si][7]) / 100 * randint(70, 90)), 1),
               'staff_tol5': d_m_t_s[kk][si][8],
               'staff_meas5': round(((d_m_t_s[kk][si][8]) / 100 * randint(70, 90)), 1),
               }
    doc.render(context)
    doc.save("template_staff_final.docx")
    file_to_save = os.path.join(os.path.dirname('template_staff_final.docx'),
                                'template_staff_final.docx')
    path_normalized = os.path.normpath(file_to_save)
    new_dir = os.path.join(os.path.dirname(path_normalized), 'протоколы по годам',
                           str(dict_sales[k][0].year), f'{dict_sales[k][0].month:02d}')
    if not os.path.exists(new_dir):
        os.makedirs(name=new_dir)
    new_file_name = new_dir + '/' + protocol_name + '.docx'
    with open('template_staff_final.docx', 'rb') as source, open(new_file_name, 'wb') as destination:
        destination.write(source.read())


def optical_level(k):
    doc = DocxTemplate("materials/template_optical_level.docx")
    protocol_number = str(dict_sales[k][0]) + '-' + str(dict_sales[k][2])
    protocol_name = str(dict_sales[k][0]) + '-' + dict_sales[k][1] + '-' + str(dict_sales[k][2])
    protocol_data = dict_sales[k][0]
    kk, si = dict_sales[k][5], dict_sales[k][1]
    context = {'protocol_number': protocol_number, 'protocol_data': protocol_data, 'instrument_type': dict_sales[k][1],
               'reestr_number': dict_sales[k][4], 'serial_number': dict_sales[k][2], 'owner': dict_sales[k][3],
               'method_pover': dict_sales[k][5], 'temper': dict_sales[k][8], 'humid': dict_sales[k][9],
               'press': dict_sales[k][10], 'etalons': dict_sales[k][6], 'operator_full_name': dict_sales[k][7],
               'metrology_param': d_o_l[kk][si][3], 'method_pover_name': d_o_l[kk][si][0],
               'to_look': d_o_l[kk][si][1], 'to_touch': d_o_l[kk][si][2],
               'tol1': d_o_l[kk][si][4], 'meas1': round(((d_o_l[kk][si][4]) + (randint(0, 11) - 11) / 10), 1),
               'tol2': d_o_l[kk][si][5], 'meas2': randint(15, 20), 'meas3': randint(15, 20),
               'tol3': d_o_l[kk][si][6], 'meas4': round(((d_o_l[kk][si][6]) / 100 * randint(80, 100)), 1),
               'meas5': randint(3, 10), 'meas6': round((randint(995, 1006) / 10), 1),
               'tol4': d_o_l[kk][si][7], 'meas7': round(((d_o_l[kk][si][7]) / 100 * randint(90, 100)), 2),
               'tol5': d_o_l[kk][si][8], 'meas8': round(((d_o_l[kk][si][8]) / 100 * randint(80, 100)), 1),
               }
    doc.render(context)
    doc.save("template_optical_level_final.docx")
    file_to_save = os.path.join(os.path.dirname('template_optical_level_final.docx'),
                                'template_optical_level_final.docx')
    path_normalized = os.path.normpath(file_to_save)
    new_dir = os.path.join(os.path.dirname(path_normalized), 'протоколы по годам',
                           str(dict_sales[k][0].year), f'{dict_sales[k][0].month:02d}')
    if not os.path.exists(new_dir):
        os.makedirs(name=new_dir)
    new_file_name = new_dir + '/' + protocol_name + '.docx'
    with open('template_optical_level_final.docx', 'rb') as source, open(new_file_name, 'wb') as destination:
        destination.write(source.read())


started_at = time.time()

for key in dict_sales:
    try:
        if dict_sales[key][1] in c_i.total_station_ver1_list \
                and (dict_sales[key][5] == 'МП АПМ 15-17' or dict_sales[key][5] == 'МП АПМ 14-17'
                     or dict_sales[key][5] == 'МП АПМ 63-17' or dict_sales[key][5] == 'МП 2511-0011-2021'
                     or dict_sales[key][5] == 'МП 2511-0007-2021'):
            total_station_ver1(key)
            count_files_created += 1
        elif dict_sales[key][1] in c_i.measuring_tape_list:
            measuring_tape(key)
            count_files_created += 1
        elif dict_sales[key][1] in c_i.staff_list:
            staff(key)
            count_files_created += 1
        elif dict_sales[key][1] in c_i.optical_level_list:
            optical_level(key)
            count_files_created += 1
        else:
            print(f'нет протокола для ({dict_sales[key][1]}), методика ({dict_sales[key][5]}), ячейка ({key + 2})')
    except Exception as exc:
        print(f'Ошибка {exc} ключ {key}')

ended_at = time.time()
elapsed = round(ended_at - started_at, 4)
print(f'процесс шел {elapsed} секунд(ы)')

print(f'обработано строк в файле - {count_lines}')
print(f'пустых строк в файле - {count_empty_lines}')
print(f'создано записей в словаре - {count_records_in_dict}')
print(f'создано протоколов - {count_files_created}')
