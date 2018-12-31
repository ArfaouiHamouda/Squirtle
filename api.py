from flask import Flask, request, jsonify
from Squirtle import Brock

app = Flask(__name__)


@app.route('/getJSON',methods=['GET'])
def get_all_items():
    model = Brock()
    return jsonify(model.get_json(download=False))


app.run(debug=True)
