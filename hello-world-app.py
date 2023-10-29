from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello world"

@app.route('/second')
def second():
    return "This is the second page"

@app.route('/third')
def third():
    return f"This is the third page"

@app.route('/<string:id>')
def dynamicfunc(id):
    return f'The ID you entered is {id}'





if __name__ == '__main__':
    app.run(debug=True, port=30000)
