from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"
app.debug = True

@app.route("/")
def index(): 
    return render_template("index.html")


@app.route("", methods=['GET', 'POST'])
def summarize():
 import nltk
 from nltk.corpus import stopwords
 from nltk.tokenize import word_tokenize, sent_tokenize
 import re
 import sys
 text = """"""
 if request.method == 'POST':
        # input text to summarize
    text = str(request.form['name_input'])
    if(len(text) == 0):
	    # flash("Please enter some text")
	    return render_template("index.html")
    else:
        # Tokenizing the text
        stopwords = set(stopwords.words('english'))
        words = word_tokenize(text)

        # creating frequency table to keep the score of each word
        freq_table = dict()
        print("hello2", file=sys.stderr)

        for word in words:
            word = word.lower()
            if word not in stopwords:
                if word in freq_table:
                    freq_table[word] += 1
                else:
                    freq_table[word] = 1
        print("hello3", file=sys.stderr)

        # creating a dictionary to keep the score of each sentence
        sentences = sent_tokenize(text)
        sentenceValue = dict()

        for sentence in sentences:
            for word, freq in freq_table.items():
                if word in sentence.lower():
                    if sentence in sentenceValue:
                        sentenceValue[sentence] += freq
                    else:
                        sentenceValue[sentence] = freq

        print("hello4", file=sys.stderr)

        sumValue = 0

        for sentence in sentenceValue:
            sumValue += sentenceValue[sentence]

        # Average value of a sentence from the original text

        average = sumValue/len(sentenceValue)

        # Storing sentences to our summary

        summary = ""
        for sentence in sentences:
            if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2*average)):
                summary += " " + sentence
        print("hello5", file=sys.stderr)

        print(str(summary), file=sys.stderr)
        flash(str(summary))
        return render_template("index.html")
