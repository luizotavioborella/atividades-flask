from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/converter_temperatura', methods=['POST'])
def converter_temperatura():
   celsius = float(request.form['celsius'])
   fh = round((celsius * 1.8) + 32, 2)
   return render_template('index.html', celsius = celsius, fh = fh)

if __name__ == '__main__':
   app.run(debug=True)