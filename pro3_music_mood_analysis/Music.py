from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators
# Imports the Google Cloud client library
from google.cloud import translate
from google.oauth2 import service_account
import re
import predict_work

app = Flask(__name__)


## classify song ##


def classify(lyrics):
    happy,sad = predict_work.predict_work(lyrics)
    return happy,sad

## translate ##
def trans(text):
    credentials = service_account.Credentials.from_service_account_file(
        'INFO6105-89d174904e2f.json')
    #Instantiates a client
    translate_client = translate.Client(credentials = credentials)
    # The target language
    target = 'en'
    # Translates some text into English
    translation = translate_client.translate(
        text,
        target_language=target)
    result = translation['translatedText']
    ##print(u'Text: {}'.format(text))
    ##print(u'Translation: {}'.format(translation['translatedText']))
    print(text)
    print(result)
    return result

##Flask##
class ReviewForm(Form):
    moviereview = TextAreaField('',[validators.DataRequired(),validators.length(min = 15)])
@app.route('/')
def home():
    form = ReviewForm(request.form)
    return render_template('home.html', form = form)

@app.route('/results', methods=['POST'])
def results():
    form = ReviewForm(request.form)
    if request.method == 'POST' and form.validate():
        ch_lyric = request.form['moviereview']
        eng_lyric = trans(ch_lyric)
        eng_lyric_processed = re.sub(r"[^a-zA-Z]", ' ', eng_lyric).lower()
        eng_lyric_processed = re.sub(r"[\n\t\s]+", ' ', eng_lyric_processed)
        happy,sad = classify(eng_lyric_processed)
        return render_template('results.html',content = eng_lyric,prediction = happy,probability = round(happy*100,2))
    return render_template('home.html',form = form)

if __name__ == '__main__':
    app.run()