from flask import Flask, jsonify, request

app = Flask(__name__)

# ---- Home Route ----
@app.route("/")
def home():
    return "Welcome to the CI/CD Flask App!"

# ---- Health Check ----
@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "OK", "service": "Flask CI/CD App"}), 200

# ---- Addition (Query Params) ----
@app.route("/add", methods=["GET"])
def add_numbers():
    """
    Example: /add?a=5&b=10
    """
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
        return jsonify({"operation": "addition", "result": a + b}), 200
    except ValueError:
        return jsonify({"error": "Invalid input, please provide integers"}), 400

# ---- Subtraction (Query Params) ----
@app.route("/subtract", methods=["GET"])
def subtract_numbers():
    """
    Example: /subtract?a=20&b=5
    """
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
        return jsonify({"operation": "subtraction", "result": a - b}), 200
    except ValueError:
        return jsonify({"error": "Invalid input, please provide integers"}), 400

# ---- Multiplication (POST) ----
@app.route("/multiply", methods=["POST"])
def multiply_numbers():
    """
    Example POST JSON: {"a": 5, "b": 6}
    """
    data = request.get_json()
    try:
        a = int(data.get("a", 0))
        b = int(data.get("b", 0))
        return jsonify({"operation": "multiplication", "result": a * b}), 200
    except (ValueError, AttributeError):
        return jsonify({"error": "Invalid input, please provide integers"}), 400

# ---- Division (POST) ----
@app.route("/divide", methods=["POST"])
def divide_numbers():
    """
    Example POST JSON: {"a": 10, "b": 2}
    """
    data = request.get_json()
    try:
        a = int(data.get("a", 0))
        b = int(data.get("b", 1))
        if b == 0:
            return jsonify({"error": "Division by zero is not allowed"}), 400
        return jsonify({"operation": "division", "result": a / b}), 200
    except (ValueError, AttributeError):
        return jsonify({"error": "Invalid input, please provide integers"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

