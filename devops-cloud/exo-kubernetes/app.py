from flask import Flask, Blueprint, jsonify

app = Flask(__name__)
main = Blueprint('main', __name__)

healthy = True


@main.route("/health", methods=['GET'])
def health():
    if healthy:
        return jsonify(status="ok"), 200
    else:
        return jsonify(status="error"), 500


@main.route("/break", methods=['GET'])
def break_app():
    global healthy
    healthy = False
    return "Health probe will now fail", 200


app.register_blueprint(main)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
