metr_par3_04 = 'СКП 3 + 0,4 * 10-6 * D'
metr_par3_05 = 'СКП (в плане) 3 + 0,5 * 10-6 * D, (по высоте) 5 + 0,5 * 10-6 * D'
metr_par25_05_30000 = 'диапазон измерений 0-30000 м, СКП (в плане)2,5 + 0,5 * 10-6 * D, (по высоте)5 + 0,5 * 10-6 * D'
metr_par3_35_30000 = 'диапазон измерений 0-30000 м, СКП (в плане) 3 + 0,5 * 10-6 * D, (по высоте) 3,5 + 0,5 * 10-6 * D'
metr_par3_5_30000 = 'диапазон измерений 0-30000 м, СКП (в плане) 3 + 0,5 * 10-6 * D, (по высоте) 5 + 0,5 * 10-6 * D'
metr_par3_03_5_30000 = 'диапазон измерений 0-30000 м, СКП (в плане) 3 + 0,3 * 10-6 * D, (по высоте) 5 + 0,5 * 10-6 * D'
metr_par25_05_1_8000 = 'диапазон измерений 0-8000 м, СКП (в плане)2,5 + 1 * 10-6 * D, (по высоте)5 + 1 * 10-6 * D'
metr_par25_05_1_30000 = 'диапазон измерений 0-8000 м, СКП (в плане)2,5 + 1 * 10-6 * D, (по высоте)5 + 1 * 10-6 * D'


dict_dopuska_GNSS_receiver = {
    'МП АПМ 78-17': {'Аппаратура геодезическая спутниковая SinoGNSS T300 plus':
                     ('Аппаратура геодезическая спутниковая SinoGNSS T300. Методика поверки', 'п. 7.1', 'п. 7.2',
                      metr_par25_05_30000, 5.0, 10.0, 2.5, 5.0, 16.0, 30.0, 8.0, 15.0, 500, 1000, 250, 500),
                     'Аппаратура геодезическая спутниковая SinoGNSS T300':
                     ('Аппаратура геодезическая спутниковая SinoGNSS T300. Методика поверки', 'п. 7.1', 'п. 7.2',
                      metr_par25_05_30000, 5.0, 10.0, 2.5, 5.0, 16.0, 30.0, 8.0, 15.0, 500, 1000, 250, 500)},
    'МП АПМ 87-15': {'Аппаратура геодезическая спутниковая NET-G5':
                     ('Аппаратура геодезическая спутниковая TOPCON NET-G5, TOPCON GR-5, TOPCON Hiper V, SOKKIA GRX2. '
                      'Методика поверки', 'п. 8.1', 'п. 8.2',
                      metr_par3_35_30000, 6.0, 7.0, 3.0, 3.5, 10.0, 20.0, 5.0, 10.0, 800, 1200, 400, 600),
                     'Аппаратура геодезическая спутниковая GR-5':
                     ('Аппаратура геодезическая спутниковая TOPCON NET-G5, TOPCON GR-5, TOPCON Hiper V, SOKKIA GRX2. '
                      'Методика поверки', 'п. 8.1', 'п. 8.2',
                      metr_par3_35_30000, 6.0, 7.0, 3.0, 3.5, 10.0, 20.0, 5.0, 10.0, 800, 1200, 400, 600),
                     'Аппаратура геодезическая спутниковая Hiper V':
                     ('Аппаратура геодезическая спутниковая TOPCON NET-G5, TOPCON GR-5, TOPCON Hiper V, SOKKIA GRX2. '
                      'Методика поверки', 'п. 8.1', 'п. 8.2',
                      metr_par3_35_30000, 6.0, 7.0, 3.0, 3.5, 20.0, 30.0, 10.0, 15.0, 800, 1200, 400, 600),
                     'Аппаратура геодезическая спутниковая GRX2':
                     ('Аппаратура геодезическая спутниковая TOPCON NET-G5, TOPCON GR-5, TOPCON Hiper V, SOKKIA GRX2. '
                      'Методика поверки', 'п. 8.1', 'п. 8.2',
                      metr_par3_35_30000, 6.0, 7.0, 3.0, 3.5, 20.0, 30.0, 10.0, 15.0, 800, 1200, 400, 600)
                     },
    'МП АПМ 01-20': {'Аппаратура геодезическая спутниковая Hiper VR':
                     ('Аппаратура геодезическая спутниковая TOPCON Hiper VR, SOKKIA GRX3. Методика поверки',
                      'п. 7.1', 'п. 7.2', metr_par3_5_30000,
                      6.0, 10.0, 3.0, 5.0, 10.0, 20.0, 5.0, 10.0, 500, 1000, 250, 500),
                     'Аппаратура геодезическая спутниковая GRX3':
                     ('Аппаратура геодезическая спутниковая TOPCON Hiper VR, SOKKIA GRX3. Методика поверки',
                      'п. 7.1', 'п. 7.2', metr_par3_5_30000,
                      6.0, 10.0, 3.0, 5.0, 10.0, 20.0, 5.0, 10.0, 500, 1000, 250, 500)
                     },
    'МП АПМ 55-20': {'Аппаратура геодезическая спутниковая OC-111':
                     ('Аппаратура геодезическая спутниковая 4GNSS серии OC-110, OC-210, OC-123M, FlyBox. '
                      'Методика поверки', 'п. 7.1', 'п. 7.2', metr_par25_05_1_8000,
                      5.0, 10.0, 2.5, 5.0, 20.0, 40.0, 10.0, 20.0, 1000, 2000, 500, 1000),
                     'Аппаратура геодезическая спутниковая OC-112':
                     ('Аппаратура геодезическая спутниковая 4GNSS серии OC-110, OC-210, OC-123M, FlyBox. '
                      'Методика поверки', 'п. 7.1', 'п. 7.2', metr_par25_05_1_30000,
                      5.0, 10.0, 2.5, 5.0, 16.0, 30.0, 8.0, 15.0, 1000, 2000, 500, 1000),
                     'Аппаратура геодезическая спутниковая OC-113':
                     ('Аппаратура геодезическая спутниковая 4GNSS серии OC-110, OC-210, OC-123M, FlyBox. '
                      'Методика поверки', 'п. 7.1', 'п. 7.2', metr_par25_05_1_30000,
                      5.0, 10.0, 2.5, 5.0, 16.0, 30.0, 8.0, 15.0, 1000, 2000, 500, 1000),
                     'Аппаратура геодезическая спутниковая OC-213':
                     ('Аппаратура геодезическая спутниковая 4GNSS серии OC-110, OC-210, OC-123M, FlyBox. '
                      'Методика поверки', 'п. 7.1', 'п. 7.2', metr_par25_05_1_30000,
                      5.0, 10.0, 2.5, 5.0, 16.0, 30.0, 8.0, 15.0, 1000, 2000, 500, 1000),
                     'Аппаратура геодезическая спутниковая OC-123M':
                     ('Аппаратура геодезическая спутниковая 4GNSS серии OC-110, OC-210, OC-123M, FlyBox. '
                      'Методика поверки', 'п. 7.1', 'п. 7.2', metr_par25_05_1_30000,
                      5.0, 10.0, 2.5, 5.0, 16.0, 30.0, 8.0, 15.0, 1000, 2000, 500, 1000),
                     'Аппаратура геодезическая спутниковая FlyBox':
                     ('Аппаратура геодезическая спутниковая 4GNSS серии OC-110, OC-210, OC-123M, FlyBox. '
                      'Методика поверки', 'п. 7.1', 'п. 7.2', metr_par25_05_1_30000,
                      5.0, 10.0, 2.5, 5.0, 16.0, 30.0, 8.0, 15.0, 1000, 2000, 500, 1000)
                     },
    'МИ 2408-97': {'Аппаратура геодезическая спутниковая GRX2':
                   ('Аппаратура пользователей космических навигационных систем геодезическая. Методика поверки',
                    'п. 6.1', 'п. 6.2', metr_par3_05, 0, 0, 3.0, 5.0, 0, 0, 10.0, 15.0, 0, 0, 0, 0),
                   'Аппаратура геодезическая спутниковая Hiper SR':
                   ('Аппаратура пользователей космических навигационных систем геодезическая. Методика поверки',
                    'п. 6.1', 'п. 6.2', metr_par3_05, 0, 0, 3.0, 5.0, 0, 0, 10.0, 15.0, 0, 0, 0, 0),
                   'Аппаратура геодезическая спутниковая Hiper V':
                   ('Аппаратура пользователей космических навигационных систем геодезическая. Методика поверки',
                    'п. 6.1', 'п. 6.2', metr_par3_05, 0, 0, 3.0, 5.0, 0, 0, 10.0, 15.0, 0, 0, 0, 0),
                   'Аппаратура геодезическая спутниковая GR-5':
                   ('Аппаратура пользователей космических навигационных систем геодезическая. Методика поверки',
                    'п. 6.1', 'п. 6.2', metr_par3_05, 0, 0, 3.0, 5.0, 0, 0, 10.0, 15.0, 0, 0, 0, 0)
                   },
    'ГОСТ Р 8.793-2012': {'Аппаратура геодезическая спутниковая Hiper HR':
                          ('Аппаратура спутниковая геодезическая. Методика поверки', 'п. 8.1', 'п. 8.2',
                           metr_par3_03_5_30000, 9.0, 15.0, 3.0, 5.0, 15.0, 30.0, 5.0, 10.0, 1200, 1800, 400, 600),
                          'Аппаратура геодезическая спутниковая GCX3':
                          ('Аппаратура спутниковая геодезическая. Методика поверки', 'п. 8.1', 'п. 8.2',
                           metr_par3_5_30000, 9.0, 15.0, 3.0, 5.0, 15.0, 30.0, 5.0, 10.0, 1200, 1800, 400, 600)}
}
