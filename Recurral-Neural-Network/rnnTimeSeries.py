import tensorflow as tf
from tensorflow.python.keras.models import Sequential, model_from_yaml
from tensorflow.python.keras.layers import Dense, Dropout, LSTM, LSTM, BatchNormalization
from tensorflow.python.keras.callbacks import TensorBoard, ModelCheckpoint
import pandas as pd
import numpy as np
from itertools import combinations
from sklearn import preprocessing
from collections import deque
import random
import time
import talib

stocks = ['AKBNK', 'GARAN', 'HALKB', 'ISCTR']

dataFrequency = '4H'
from_symbol = 'CHF'
to_symbol = 'JPY'
filepath = '/home/cem/PycharmProjects/untitled/functions/store/DataBist/freq_{}/'.format(
    dataFrequency)
mode = 'backtest'  # backtest or live-prediction or zipline

cutForMin = 0
cutForMax = 0.004
checkLength = 10

SEQ_LEN = 20
FUTURE_PERIOD_PREDICT = 2
RATIO_TO_PREDICT = 'ISCTR'
EPOCHS = 50
BATCH_SIZE = 64
mode = '1'
NAME = '{}-{}-{}-MODE-{}-SEQ-{}-PRED-{}'.format(dataFrequency, RATIO_TO_PREDICT, mode, SEQ_LEN,
                                                FUTURE_PERIOD_PREDICT,
                                                int(time.time()))


def classify(current, future, mode=mode):
    if mode == '1':
        if float(future) > float(current):
            return 1
        else:
            return 0
    elif mode == '2':
        ratio = (float(future) - float(current)) / float(current)
        if ratio > 0.005:
            return 2
        elif ratio >= 0:
            return 1
        elif ratio > -0.005:
            return 0
        elif ratio <= -0.005:
            return -1
    elif mode == '3':
        ratio = (float(future) - float(current)) / float(current)
        if ratio > 0.005:
            return 2
        elif ratio >= 0:
            return 1
        elif ratio > -0.005:
            return 0
        elif ratio <= -0.005:
            return -1


def preprocess_df(df):
    df = df.drop('future', 1)
    for col in df.columns:
        if (col != 'target' and
                not col.endswith('HBTRENDMODE') and
                not col.endswith('CDLRISEFALL3METHODS')):
            df[col] = df[col].pct_change()
            df.dropna(inplace=True)
            df[col] = preprocessing.scale(df[col].values)
    df.dropna(inplace=True)
    sequential_data = []
    prev_days = deque(maxlen=SEQ_LEN)
    for i in df.values:
        prev_days.append([n for n in i[:-1]])
        if len(prev_days) == SEQ_LEN:
            sequential_data.append([np.array(prev_days), i[-1]])

    random.shuffle(sequential_data)
    buys = []
    sells = []

    for seq, target in sequential_data:
        if target == 0:
            sells.append([seq, target])
        if target == 1:
            buys.append([seq, target])

    random.shuffle(buys)
    random.shuffle(sells)

    lower = min(len(buys), len(sells))

    buys = buys[:lower]
    sells = sells[:lower]

    sequential_data = buys + sells
    random.shuffle(sequential_data)

    X = []
    y = []

    for seq, target in sequential_data:
        X.append(seq)
        y.append(target)
    return np.array(X), y


main_df = pd.DataFrame()
for stock in stocks:
    symbol = stock
    if dataFrequency == '1h':
        df = pd.read_hdf('{}{}.E.h5'.format(filepath, symbol), key='table')
    # df = df.resample("1min").mean()
    else:

        df = pd.read_hdf('{}Bist.h5'.format(filepath), key=symbol)

    df.index.name = 'time'
    df.rename(columns={"close": "{}".format(symbol) + '_close',
                       "high": "{}".format(symbol) + '_high',
                       "low": "{}".format(symbol) + '_low',
                       "open": "{}".format(symbol) + '_open',
                       "volume": "{}".format(symbol) + 'volume'
                       }, inplace=True
              )
    df['{}_HBTRENDMODE'.format(symbol)] = talib.HT_TRENDMODE(df['{}_close'.format(symbol)])
    df['{}_TSF'.format(symbol)] = talib.TSF(df['{}_close'.format(symbol)], timeperiod=14)
    df['{}_CDLRISEFALL3METHODS'.format(symbol)] = talib.CDLRISEFALL3METHODS(
        open=df['{}_open'.format(symbol)],
        high=df['{}_high'.format(symbol)],
        low=df['{}_low'.format(symbol)],
        close=df['{}_close'.format(symbol)
        ])

    if len(main_df) == 0:
        main_df = df
    else:
        main_df = main_df.join(df)

main_df['future'] = main_df['{}_close'.format(RATIO_TO_PREDICT)].shift(-FUTURE_PERIOD_PREDICT)
main_df['target'] = list(
    map(classify, main_df['{}_close'.format(RATIO_TO_PREDICT)], main_df['future']))

times = sorted(main_df.index.values)
last_5pct = times[-int(0.05 * len(times))]
last_10pct = times[-int(0.1 * len(times))]

cutforValidationData = last_10pct
validation_main_df = main_df[(main_df.index >= cutforValidationData)]
main_df = main_df[(main_df.index < cutforValidationData)]

train_x, train_y = preprocess_df(main_df)
validation_x, validation_y = preprocess_df(validation_main_df)
# print('validation_x id: ', validation_main_df)
print("train data: {}".format(len(train_x)), "validation : ", '{}'.format(len(validation_x)))
print("Dont buys: {}, ".format(train_y.count(0)),
      "buys: {}".format(train_y.count(1)))
print("VALIDATION Dont buys: {}".format(validation_y.count(0)),
      "buys : {}".format(validation_y.count(1)))
train_y = np.array(train_y)
validation_y = np.array(validation_y)
model = Sequential()
model.add(LSTM(128, input_shape=(train_x.shape[1:]), return_sequences=True))
model.add(Dropout(0.2))
model.add(BatchNormalization())

model.add(LSTM(128, return_sequences=True))
model.add(Dropout(0.1))
model.add(BatchNormalization())

model.add(LSTM(128))
model.add(Dropout(0.2))
model.add(BatchNormalization())

model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(2, activation='softmax'))

opt = tf.keras.optimizers.Adam(lr=1e-3, decay=1e-6)

model.compile(loss='sparse_categorical_crossentropy',
              optimizer=opt,
              metrics=['accuracy'])

tensorboard = TensorBoard(log_dir='logs/{}'.format(NAME))

filepath = "RNN_Final-{epoch:02d}-{val_acc:.3f}"

checkpoint = ModelCheckpoint("models/{}.model".format(filepath,
                                                      monitor='val_acc',
                                                      verbose=1,
                                                      save_best_only=True,
                                                      mode='max'))

history = model.fit(train_x, train_y,
                    batch_size=BATCH_SIZE,
                    epochs=EPOCHS,
                    validation_data=(validation_x, validation_y),
                    callbacks=[tensorboard, checkpoint])

model.save('{}'.format(NAME))
