from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', deepfake = "n/a", confidence = "n/a")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
