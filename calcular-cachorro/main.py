from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/converter_idade', methods=['POST'])
def converter_idade():
   idade = int(request.form['idade'])
   convert = 24 + (idade - 2) * 5
   return render_template('index.html', idade = idade, convert = convert)

if __name__ == '__main__':
   app.run(debug=True)