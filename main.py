from flask import Flask, render_template, request
from googletrans import Translator, LANGUAGES
 
 
app = Flask(__name__)
translator = Translator()
 
 
@app.route('/')
def index():
   return render_template('index.html', languages=LANGUAGES)
 
 
@app.route('/translate', methods=['POST'])
def translate():
   text = request.form['text']
   source_lang = request.form['source_lang']
   target_lang = request.form['target_lang']
 
 
   # Translate the text from the source language to the target language
   translated_text = translator.translate(text, src=source_lang, dest=target_lang).text
 
 
   return render_template('index.html', text=text, translated_text=translated_text, source_lang=LANGUAGES[source_lang],
                          target_lang=LANGUAGES[target_lang], languages=LANGUAGES)
 
 
if __name__ == '__main__':
   app.run(debug=True)
