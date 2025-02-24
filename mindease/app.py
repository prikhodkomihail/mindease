from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/emotions', methods=['GET'])
def get_emotions():
    emotions = ["happy", "anxious", "overwhelmed", "sad", "angry", "surprised", "calm", "nervous", "depressed"]
    return jsonify(emotions)

@app.route('/log_emotions', methods=['POST'])
def log_emotions():
    data = request.get_json()
    return jsonify({'message': 'Emotion logged successfully', 'data': data}), 201

if __name__ == '__main__':
    app.run(debug=True)