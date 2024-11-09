from flask import Flask

app = Flask(__name__, template_folder='views')

@app.route('/')
def index():
    return 'Hola mundo'

if __name__ == '__main__':
    app.run(debug=True)