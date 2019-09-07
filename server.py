from flask import Flask, render_template, url_for, request, session, redirect
import warnings
import fileslist

warnings.filterwarnings("ignore")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    projectpath = request.form['projectFilepath']
    rmse, acc = fileslist.deploy(projectpath)
    return render_template('results.html', rmse=rmse, acc=acc)


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.debug = True
    app.run(host='localhost', port="5001")