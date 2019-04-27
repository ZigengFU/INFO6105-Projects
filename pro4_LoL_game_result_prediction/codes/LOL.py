import keras
from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators
from sklearn.externals import joblib
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.layers.merge import concatenate
from keras.models import Sequential, Model
from keras.layers import Dense, Embedding, Activation, merge, Input, Lambda, Reshape
from keras.layers import Convolution1D, Flatten, Dropout, MaxPool1D, GlobalAveragePooling1D
from keras.layers import LSTM, GRU, TimeDistributed, Bidirectional
from keras.utils.np_utils import to_categorical
from keras import initializers
from keras import backend as K
from keras.engine.topology import Layer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import csv

app = Flask(__name__)
#Flask#
class ReviewForm(Form):
    T1 = TextAreaField('',[validators.DataRequired(),validators.length(min = 1)])
    T2 = TextAreaField('',[validators.DataRequired(),validators.length(min = 1)])

@app.route('/')
def home():
    form = ReviewForm(request.form)
    return  render_template('home.html',form = form)

@app.route('/results', methods=['POST'])
def results():
    form = ReviewForm(request.form)
    if request.method == 'POST' and form.validate():
        Team1 = request.form['T1']
        Team2 = request.form['T2']
        result = prediction(Team1,Team2)
        return render_template('results.html', team1 = Team1, team2 = Team2, prediction = result, probability = round(result*100,2))
    return render_template('home.html', form = form)

def prediction(str1, str2):
    keras.backend.clear_session()
    all_team_data = pd.read_csv('teamDataAfterClean.csv')
    team_data_array = np.array(all_team_data)
    tmplineRate1 = []
    tmplineRate2 = []
    tmpdataline = []
    dataline = []
    for line in team_data_array:
        if line[0] == str1:
            tmpline2 = line[2:22]
            if line[1] == 'LMS':
                tmpline2 = tmpline2 * 0.7
            if line[1] == 'LCS' or line[1] == 'LEC':
                tmpline2 = tmpline2 * 0.8
            tmplineRate1 = line[22:27]
            for x in tmpline2:
                tmpdataline.append(x)

    for line in team_data_array:
        if line[0] == str2:
            print(line[0], '  ', str2)
            tmpline2 = line[2:22]
            if line[1] == 'LMS':
                tmpline2 = tmpline2 * 0.7
            if line[1] == 'LCS' or line[1] == 'LEC':
                tmpline2 = tmpline2 * 0.8
            tmplineRate2 = line[22:27]
            for x in tmpline2:
                tmpdataline.append(x)

    # print(tmpdataline)
    for x in tmplineRate1:
        tmpdataline.append(x)
    for x in tmplineRate2:
        tmpdataline.append(x)

    print(tmpdataline)

    dataline.append(tmpdataline)

    final_x = np.array(dataline)

    model_mlp = joblib.load('train_model_mlp.m')
    model_linear = joblib.load('train_model_linear.m')
    model_tree = joblib.load('train_model_tree.m')
    result1 = model_mlp.predict(final_x)
    result2 = model_linear.predict(final_x)
    result3 = model_tree.predict(final_x)
    ans = 0

    ans = ans + result1[0][1]
    ans = ans + result2[0]
    ans = ans + result3[0]
    ans = ans / 3

    if ans > 0.5:
        return (result1[0][1] + 0.671957671957672 + 0.5714285714285714) / 3
    else:
        return (result1[0][0] + 0.671957671957672 + 0.5714285714285714) / 3

if __name__ == '__main__':
    app.run(debug=True)
