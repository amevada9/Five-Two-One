import flask
from flask import Flask
#from flask.ext.bootstrap import Bootstrap  

app = Flask(__name__)

#bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return flask.render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)