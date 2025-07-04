# Store chat messages in memory (basic example)
chat_history = []

@app.route("/api/chat", methods=["POST"])
def receive_chat():
    data = request.json
    if not data or "username" not in data or "message" not in data:
        return jsonify(success=False, error="Missing data"), 400

    print(f"💬 {data['username']}: {data['message']}")
    chat_history.append(data)

    # Optional: cap chat memory
    if len(chat_history) > 50:
        chat_history.pop(0)

    return jsonify(success=True)

@app.route("/api/chat/latest", methods=["GET"])
def get_latest_chat():
    if not chat_history:
        return jsonify(success=False, message="No chat"), 404
    return jsonify(success=True, data=chat_history[-1])
