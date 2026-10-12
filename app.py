from flask import Flask, jsonify, request

app = Flask(__name__)

orders = [
    {"id": 1, "item": "Laptop", "quantity": 1},
    {"id": 2, "item": "Keyboard", "quantity": 2}
]


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "application": "OrderHub",
        "message": "OrderHub API is running",
        "version": "1.0"
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "UP"}), 200


@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(orders), 200


@app.route("/orders", methods=["POST"])
def create_order():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "A JSON object is required"}), 400

    item = data.get("item")
    quantity = data.get("quantity")

    if not isinstance(item, str) or not item.strip():
        return jsonify({"error": "Item is required"}), 400

    if type(quantity) is not int or quantity <= 0:
        return jsonify({"error": "Quantity must be a positive integer"}), 400

    order = {
        "id": max((o["id"] for o in orders), default=0) + 1,
        "item": item.strip(),
        "quantity": quantity
    }

    orders.append(order)

    return jsonify(order), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
