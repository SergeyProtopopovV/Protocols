def instrument_correct(instrument):
    instrument = instrument.replace('Тахеометры электронные', 'Тахеометр электронный')
    instrument = instrument.replace('Тахеометры электронные TOPCON', 'Тахеометр электронный')
    instrument = instrument.replace('Рулетки', 'Рулетка')
    instrument = instrument.replace('СС10M', 'CC10M')
    instrument = instrument.replace('СС20M', 'CC20M')
    instrument = instrument.replace('TC30/5', 'TC30/5')
    instrument = instrument.replace('IM-', 'iM-')
    instrument = instrument.replace('Нивелиры оптико-механические с компенсатором', 'Нивелир')
    instrument = instrument.replace('Нивелиры с компенсатором', 'Нивелир')
    instrument = instrument.replace('Нивелиры оптические', 'Нивелир')
    instrument = instrument.replace('B30А', 'B30A')
    instrument = instrument.replace('Тахеометры электронные под товарным знаком TOPCON и товарным знаком "SOKKIA"',
                                    'Тахеометр электронный')
    instrument = instrument.replace('Тахеометр электронный под товарным знаком TOPCON и товарным знаком "SOKKIA"',
                                    'Тахеометр электронный')
    return instrument
