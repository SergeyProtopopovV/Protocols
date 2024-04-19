def instrument_correct(instrument):
    instrument = instrument.replace('Тахеометры электронные TOPCON', 'Тахеометр электронный')
    instrument = instrument.replace('Тахеометры электронные', 'Тахеометр электронный')
    instrument = instrument.replace('Рулетки', 'Рулетка')
    instrument = instrument.replace('TL5M', 'TL5M')
    instrument = instrument.replace('СС10M', 'CC10M')
    instrument = instrument.replace('СС20M', 'CC20M')
    instrument = instrument.replace('TC30/5', 'TC30/5')
    instrument = instrument.replace('TS30/2', 'TS30/2')
    instrument = instrument.replace('IM-', 'iM-')
    instrument = instrument.replace('Нивелиры оптико-механические с компенсатором', 'Нивелир')
    instrument = instrument.replace('Нивелиры с компенсатором', 'Нивелир')
    instrument = instrument.replace('Нивелиры оптические', 'Нивелир')
    instrument = instrument.replace('B30А', 'B30A')
    instrument = instrument.replace('Тахеометры электронные под товарным знаком TOPCON и товарным знаком "SOKKIA"',
                                    'Тахеометр электронный')
    instrument = instrument.replace('Тахеометр электронный под товарным знаком TOPCON и товарным знаком "SOKKIA"',
                                    'Тахеометр электронный')
    instrument = instrument.replace('GPS-приемник', 'Аппаратура геодезическая спутниковая')
    instrument = instrument.replace('Аппаратура спутниковая геодезическая', 'Аппаратура геодезическая спутниковая')
    instrument = instrument.replace(' TOPCON ', ' ')
    instrument = instrument.replace(' Topcon ', ' ')
    instrument = instrument.replace(' SOKKIA ', ' ')
    instrument = instrument.replace(' изм ', ' ')
    instrument = instrument.replace('Аппаратура геодезическая спутниковая SinoGNSS T300 Plus',
                                    'Аппаратура геодезическая спутниковая SinoGNSS T300 plus')
    instrument = instrument.replace('GNSS-приемники спутниковые геодезические многочастотные',
                                    'Аппаратура геодезическая спутниковая')
    instrument = instrument.replace('SinoGNSS SinoGNSS', 'SinoGNSS')
    instrument = instrument.replace('спутниковая USA', 'спутниковая')
    instrument = instrument.replace('HIPER', 'Hiper')
    instrument = instrument.replace('GPS приемник', 'Аппаратура геодезическая спутниковая')
    instrument = instrument.replace('GNSS-станции опорные спутниковые геодезические многочастотные',
                                    'Аппаратура геодезическая спутниковая')
    instrument = instrument.replace('Leica DISTO', 'DISTO')
    instrument = instrument.replace('Дальномер', 'Дальномер лазерный')
    instrument = instrument.replace('Дальномер лазерный лазерный', 'Дальномер лазерный')
    return instrument
