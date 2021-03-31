from flask import Flask
# from flask_restful import Api, Resource
from flask import request

app = Flask(__name__)



def is_prime(number):
    if number > 1:
        for n in range(2, int(number ** 0.5) + 1):
            if number % n == 0:
                return 'The number ' + str(number) + ' is not prime'
    return 'The number ' + str(number) + ' is prime'


def is_valid(number):
    return True if number > 1 else False

@app.route("/prime", methods=["GET"])
def hello():
    params = request.args.get('n')
    # print(params)
    number = int(params)
    return str(is_prime(number) if is_valid(number) else "Out of Range")


if __name__ == '__main__':
    app.run(debug=True)