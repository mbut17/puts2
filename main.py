from flask import Flask, request
from fractions import Fraction
from decimal import Decimal

app = Flask(__name__)

@app.route('/')
def index():
    return 'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n'


@app.route('/add')
def addition():
     try:
        r1=request.args.get('A',default = 0, type = Fraction)
    except ZeroDivisionError as error:
        r1='None'
    try:
        r2=request.args.get('B',default = 0, type = Fraction)
    except ZeroDivisionError as error:
        r2='None'
    if r1 == 'None' or r2 == 'None' :
        return 'None'
    else:
        a = Fraction(r1)
        b= Fraction(r2)
        res= a+b
        return str(round(float(res),3))

@app.route('/div')
def division():
    try:
        r1=request.args.get('A',default = 0, type = Fraction)
    except ZeroDivisionError as error:
        r1='None'
    try:
        r2=request.args.get('B',default = 0, type = Fraction)
    except ZeroDivisionError as error:
        r2='None'
    if r1 == 'None' or r2 == 'None' :
        return 'None'
    else:
        a = Fraction(r1)
        b= Fraction(r2)
        try:
            res= a/b
            return(str(round(float(res),3)))
        except ZeroDivisionError as error:
            return 'None'


@app.route('/mul')
def multiplication():
    try:
        r1=request.args.get('A',default = 0, type = Fraction)
    except ZeroDivisionError as error:
        r1='None'
    try:
        r2=request.args.get('B',default = 0, type = Fraction)
    except ZeroDivisionError as error:
        r2='None'
    if r1 == 'None' or r2 == 'None' :
        return 'None'
    else:
        a = Fraction(r1)
        b= Fraction(r2)
        res= a*b
        return(str(round(float(res),3)))

@app.route('/sub')
def subtraction():
    try:
        r1=request.args.get('A',default = 0, type = Fraction)
    except ZeroDivisionError as error:
        r1='None'
    try:
        r2=request.args.get('B',default = 0, type = Fraction)
    except ZeroDivisionError as error:
        r2='None'
    if r1 == 'None' or r2 == 'None' :
        return 'None'
    else:
        a = Fraction(r1)
        b= Fraction(r2)
        res= a-b
        return(str(round(float(res),3)))


if __name__ == "__main__":
    app.run()
