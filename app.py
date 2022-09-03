from flask import Flask,  render_template


app = Flask(__name__)


# Index
@app.route('/')
def index():
    return render_template('home.html')


# Hireme
@app.route('/hireme')
def about():
    return render_template('hireme.html')

# porjects
@app.route('/projects')
def projects():
    return render_template('projects.html')



if __name__ == '__main__':
    app.secret_key='secret1234'
    app.run(app.run debug=True)
