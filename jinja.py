from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<string:a>/<string:b>")
def head (a,b):
    return render_template("index.html", number1=a, number2=b)

@app.route('/numbers/<string:num1>/<string:num2>')
def number(num1,num2):
    if num1.isdigit() and num2.isdigit():
        num1=int(num1)
        num2=int(num2)

        return render_template("body.html", value1=num1, value2=num2, sum=num1+num2)
    
    else:
        return "Please enter numbers"







if __name__ == "__main__":
    app.run(debug=True, port=30000)
