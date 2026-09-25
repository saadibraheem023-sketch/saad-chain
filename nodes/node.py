from flask import Flask, jsonify, request
from blockchain.block import Block
from blockchain.core import Blockchain   # <--- أضف هذا السطر
import requests
import uuid
from flask import render_template

import sys

# ... في بداية الملف ...
port = int(sys.argv[1]) if len(sys.argv) > 1 else 5005

# ... بعد تعريف blockchain = Blockchain() ...
# اجعل كل عقدة تستخدم قاعدة بيانات خاصة بها



app = Flask(__name__)

node_id = str(uuid.uuid4()).replace("-", "")

blockchain = Blockchain(db_name=f'blockchain_{port}.db')

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
    transaction_data = request.get_json(silent=True) or request.form
    
    sender = transaction_data.get('sender')
    receiver = transaction_data.get('receiver')
    amount = transaction_data.get('amount')
    signature = transaction_data.get('signature')  # التوقيع الجديد
    
    if not sender or not receiver or not amount:
        return jsonify({"message": "بيانات ناقصة"}), 400
    
    success, message = blockchain.add_transaction(sender, receiver, amount, signature)
    
    if not success:
        return jsonify({"message": message}), 400
    
    return jsonify({"message": message}), 201




@app.route("/valid", methods=["GET"])
def valid():

    valid = blockchain.is_chain_valid(
        blockchain.chain
    )

    return jsonify({
        "valid": valid
    })
# ========== P2P Network ==========

@app.route('/nodes/register', methods=['POST'])
def register_node():
    """تسجيل عقدة جديدة في الشبكة"""
    nodes_data = request.get_json()
    if not nodes_data or 'nodes' not in nodes_data:
        return jsonify({"message": "بيانات غير صحيحة"}), 400
    
    for node in nodes_data['nodes']:
        peers.add(node)
    
    return jsonify({
        "message": "تم تسجيل العقد",
        "total_nodes": list(peers)
    }), 201

@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    """التوصل إلى إجماع: استبدال السلسلة الحالية بأطول سلسلة في الشبكة"""
    replaced = False
    for peer in peers:
        try:
            response = requests.get(f'{peer}/chain')
            if response.status_code == 200:
                data = response.json()
                if data['length'] > len(blockchain.chain):
                    # استبدال السلسلة الحالية
                    blockchain.chain = [Block(**b) for b in data['chain']]
                    replaced = True
        except:
            continue
    
    return jsonify({
        "message": "تم تحديث السلسلة" if replaced else "السلسلة الحالية هي الأطول",
        "chain": [b.to_dict() for b in blockchain.chain],
        "length": len(blockchain.chain)
    }), 200

import sys

if __name__ == "__main__":

    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5005

    app.run(
        host="127.0.0.1",
        port=port,
        debug=False
    )