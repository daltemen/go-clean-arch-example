from flask_api import FlaskAPI, status

app = FlaskAPI(__name__)


@app.route("/")
def index():
    return "Hi Mi Aguila"


@app.route("/health")
def health():
    return "Mi Aguila Health"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777, debug=True)
