from flask import Flask, jsonify, request
from blockchain.block import Block
from blockchain.core import Blockchain   # <--- أضف هذا السطر
import requests
import uuid


app = Flask(__name__)

node_id = str(uuid.uuid4()).replace("-", "")

blockchain = Blockchain()

peers = set()


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


@app.route("/transaction", methods=["POST"])
def add_transaction():

    data = request.get_json()

    required = [
        "sender",
        "receiver",
        "amount"
    ]

    if not all(field in data for field in required):
        return "Missing fields", 400

    index = blockchain.add_transaction(
        data["sender"],
        data["receiver"],
        data["amount"]
    )

    return jsonify({
        "message": f"Transaction will be added to block {index}"
    }), 201


@app.route("/chain", methods=["GET"])
def get_chain():

    response = {
        "chain": blockchain.chain,
        "length": len(blockchain.chain)
    }

    return jsonify(response), 200


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