from flask import Flask
from random import randint
import sys

from projects.Calculator.calculator import Calculator

app = Flask(__name__)
my_calculaor = Calculator()

@app.route('/')
def hello():
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    message = "{} + {} = {}".format(num1, num2, my_calculaor.add(num1, num2))
    return message

print("The value of __name__ is: ", repr(__name__))
print("Python version: ", sys.version)

if __name__ == '__main__':
    print("Running the application")
    app.run()
