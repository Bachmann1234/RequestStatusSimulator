import time
from flask import Flask, request
app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return ''


@app.route('/<code>', methods=['GET', 'POST'])
def wait_request(code):
    wait_time_param = request.args.get('wait', '0')
    try:
        wait_time = int(wait_time_param)
    except ValueError:
        return "Wait Time {} is invalid".format(wait_time_param)
    time.sleep(wait_time)
    return "The status of this request should be {}. I waitied {} seconds".format(code, wait_time), int(code)

if __name__ == '__main__':
    app.run(debug=True)
