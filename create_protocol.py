# импорт библиотеки pandas
import pandas as pd
import pprint

# Загружаем ваш файл в переменную `file` / вместо 'example' укажите название свого файла из текущей директории
file = 'matherials/POV-ГСИ.XLS'

# Загружаем spreadsheet в объект pandas
xl = pd.ExcelFile(file)

# # Печатаем название листов в данном файле
# print(xl.sheet_names)

# Загрузить лист в DataFrame по его имени: df1
df1 = xl.parse('Продажа')

print(df1.loc[24410])
# print(df1.loc[24410][2])
# print(df1.loc[100][13])
print(str(df1.loc[100][13].year) + str(df1.loc[100][13].month) + str(df1.loc[100][13].day))
# print(type(df1.loc[100][13]))

dict_sales = {}

for i in range(24400, 24411):
    item_data = str(df1.loc[100][13].year) + str(df1.loc[100][13].month) + str(df1.loc[100][13].day)
    instrument = str(df1.loc[i][0]) + " " + str(df1.loc[i][1])
    dict_sales[i] = (item_data, instrument, df1.loc[i][2], df1.loc[i][22], df1.loc[i][23], df1.loc[i][24],
                     df1.loc[i][30], df1.loc[i][31], df1.loc[i][32], df1.loc[i][33])

pprint.pprint(dict_sales)
