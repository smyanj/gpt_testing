from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock data for Python learning resources
resources = [
    {
        "title": "Python Crash Course",
        "video": "Introduction to Python",
        "author": "Eric Matthes",
        "link": "https://www.example.com/python-crash-course"
    },
    {
        "title": "Automate the Boring Stuff with Python",
        "video": "Python Programming",
        "author": "Al Sweigart",
        "link": "https://www.example.com/automate-the-boring-stuff"
    },
    {
        "title": "Python for Data Science",
        "video": "Data Science with Python",
        "author": "John Doe",
        "link": "https://www.example.com/python-data-science"
    }
]

@app.route('/api/resources', methods=['GET'])
def get_resources():
    return jsonify(resources)

if __name__ == '__main__':
    app.run(port=5000)