from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import json
from sklearn.metrics import mean_absolute_error as mae
from sklearn.model_selection import train_test_split as tts

def run_model(mood):
    reactions = open(mood + '_reactions.data', 'r').read()
    reacts = []
    for reaction in reactions:
        try:
            reacts.append(int(reaction.replace(' ', '').replace('\n', '')))
        except:
            pass

    print(len(reacts))
    x = pd.read_json(mood + '_songs.data')
    print(x.describe())

    x['cow'] = x.mode * x.energy
    x['result'] = reacts
    x = x[x.result != 5]

    x['is_train'] = np.random.uniform(0, 1, len(x)) <= .75
    train, test = x[x['is_train']==True], x[x['is_train']==False]

    drops = ['name', 'result', 'id']

    Y_train = train.result
    X_train = train.drop(drops, axis=1)

    Y_val = test.result
    X_val = test.drop(drops, axis=1)

    model = RandomForestClassifier(n_jobs=-1, random_state=0)
    model.fit(X_train, Y_train)
    predictions = model.predict(X_val)

    c = 0
    for num in range(len(X_val)):
        if predictions[num] != Y_val.iloc[num]:
            print(x.loc[num, 'name'])
        else:
            c += 1
    print('ACCURACY: ' + '{:.3f}'.format(float(c)/len(predictions) * 100) + "%")

run_model('happy')
