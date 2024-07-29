# mock_api.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/learn_python', methods=['GET'])
def learn_python():
    resources = {
        "resources": [
            {"title": "Official Python Documentation", "url": "https://docs.python.org/3/"},
            {"title": "Learn Python - Full Course for Beginners [Tutorial]", "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"},
            {"title": "Python for Beginners", "url": "https://www.learnpython.org/"},
        ]
    }
    return jsonify(resources)

def learn_compliance():
    pass

if __name__ == '__main__':
    app.run(port=5001)


