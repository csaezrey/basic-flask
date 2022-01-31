from flask import render_template, request, json
from wallet.model import Wallet, create_wallet, read_wallet, update_wallet, delete_wallet
from app import app

@app.route("/")
def index(id="-"):
    id = request.args.get('id',id)
    return "Wallet code: {}".format(id)

@app.route("/create",methods = ['POST'])
def create():
    data = json.loads(request.data)
    owner_id = data['owner_id']
    amount = data['amount']
    wallet = create_wallet(owner_id,amount)
    return wallet.to_JSON()

@app.route("/read",methods = ['POST'])
def read(id="0"):
    id = request.args.get('id',id)
    wallet = read_wallet(id)
    return wallet.to_JSON()

@app.route("/update",methods = ['POST'])
def update():
    data = json.loads(request.data)
    id = data['id']
    amount = data['amount']
    wallet = update_wallet(id,amount)
    return wallet.to_JSON()

@app.route("/delete",methods = ['POST'])
def delete():
    data = json.loads(request.data)
    id = data['id']
    delete_wallet(id)
    return "Wallet delete: {}".format(id), 200

@app.route("/readWallet",methods = ['GET'])
def readWallet(id="0"):
    id = request.args.get('id',id)
    wallet = read_wallet(id)
    return render_template("read.html", id = id, owner = wallet.owner_id, amount = wallet.amount)