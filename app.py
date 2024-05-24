from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    # Ambil data dari formulir
    mode = request.form['mode']
    link = request.form['link']
    # Lakukan operasi sesuai dengan mode yang dipilih
    # Implementasikan operasi seperti yang Anda inginkan
    result = "Result"
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
