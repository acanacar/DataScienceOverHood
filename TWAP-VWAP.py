import pandas as pd

stockpath = '/home/cem/PycharmProjects/DataScienceOverHood/stockBankA_train.csv'

df = pd.read_csv(stockpath, sep=',')


def vwap(data, skipna):
    data['priceForVWAP'] = (data['High'] + data['Close']) / 2
    data['price-cross-volume'] = data['priceForVWAP'] * data['Volume']
    sumdata = data.sum(axis=0, skipna=skipna)
    return sumdata['price-cross-volume'] / sumdata['Volume']


def twap(data):
    data['priceForTWAP'] = (data['High'] + data['Close']) / 2
    return data['priceForTWAP'].mean()
