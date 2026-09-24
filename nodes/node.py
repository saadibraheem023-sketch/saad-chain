from flask import Flask, jsonify, request
from blockchain.block import Block
from blockchain.core import Blockchain   # <--- أضف هذا السطر
import requests
import uuid


app = Flask(__name__)

node_id = str(uuid.uuid4()).replace("-", "")

blockchain = Blockchain()

peers = set()

from flask import render_template

@app.route("/explorer", methods=["GET"])
def explorer():
    return render_template("index.html", chain=blockchain.chain)


@app.route("/mine", methods=["GET"])
def mine():

    previous_block = blockchain.get_latest_block()

    previous_proof = previous_block.proof

    proof = blockchain.proof_of_work(
        previous_proof
    )

    previous_hash = blockchain.hash(previous_block)

    # Mining reward
    blockchain.add_transaction(
        sender="0",
        receiver=node_id,
        amount=10
    )

    block = blockchain.mine_block(
        proof,
        previous_hash
    )

    response = {
        "message": "New block mined",
        "block": block.to_dict()  # <--- أضف .to_dict() هنا
}
    return jsonify(response), 200
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to Saad Chain!",
        "total_blocks": len(blockchain.chain),
        "chain": [block.to_dict() for block in blockchain.chain]
    }), 200
@app.route("/chain", methods=["GET"])
def get_chain():
    response = {
        "chain": [block.to_dict() for block in blockchain.chain],
        "length": len(blockchain.chain)
    }
    return jsonify(response), 200






from flask import request, jsonify

@app.route('/transaction', methods=['POST'])
def add_transaction():
    # 1. محاولة قراءة البيانات كـ JSON (إذا جاءت من Postman)
    transaction_data = request.get_json(silent=True)
    
    # 2. إذا لم تكن JSON، اقرأها كـ Form Data (إذا جاءت من المتصفح)
    if not transaction_data:
        transaction_data = request.form
    
    # 3. الآن نستخرج البيانات (سواء كانت من JSON أو Form)
    sender = transaction_data.get('sender')
    receiver = transaction_data.get('receiver')
    amount = transaction_data.get('amount')
    
    # 4. التحقق من وجود البيانات
    if not sender or not receiver or not amount:
        return jsonify({"message": "Missing data"}), 400
    
    # 5. إضافة المعاملة
    blockchain.add_transaction(sender, receiver, amount)
    
    return jsonify({"message": "Transaction added successfully"}), 201




@app.route("/valid", methods=["GET"])
def valid():

    valid = blockchain.is_chain_valid(
        blockchain.chain
    )

    return jsonify({
        "valid": valid
    })


import sys

if __name__ == "__main__":

    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5005

    app.run(
        host="127.0.0.1",
        port=port,
        debug=False
    )