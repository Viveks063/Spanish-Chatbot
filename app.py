from googletrans import Translator
from flask import Flask, render_template, request

translator=Translator()

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/', methods=['GET','POST'] )
def index():
    translate=None
    if request.method=='POST':
        user_input = request.form['user_input']
        if user_input.lower() == 'exit':
            return "Chatbot: Goodbye!"
        else:
            translate = translator.translate(user_input, src='en', dest='es').text
    
    return render_template('index.html',translate=translate)
    
if __name__ == '__main__':
    app.run(debug=True)
