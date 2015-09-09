from flask import Flask
app = Flask(__name__)

@app.route('/<code>', methods=['GET', 'POST'])
def request(code):
    return "The status of this request should be {}".format(code), int(code)

if __name__ == '__main__':
    app.run()