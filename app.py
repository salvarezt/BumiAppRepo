import src
from flask import Flask, jsonify, request, make_response
from flask.helpers import send_from_directory
from flask_cors import CORS

# Ini app.
app = Flask(__name__)

# Cors.
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
  return send_from_directory('./static', path)

# Main page.
@app.route('/')
def root():
    """
    Return the frontend of the application.
    """
    return send_from_directory("./static", 'index.html')

@app.route("/api/status", methods = ["GET"])
def status():
    """
    App Status
    """
    return jsonify({'status' : 200})

if __name__ == '__main__':
    app.run(debug=False)