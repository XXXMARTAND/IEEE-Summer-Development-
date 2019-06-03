from flask import Flask, request, jsonify, render_template
import random 

app = Flask(__name__)

def rdice():
	x = random.randint(1,6)
	return x

def rcoin():
	a = random.randint(0,1)
	if a==0:
		result = "TAILS"
	else:
		result = "HEADS"

	return result


@app.route("/")
def index():
	return render_template('index1.html')

@app.route("/dice", methods = ["GET","POST"])
def dice():
	if (request.method=="GET"):
		value = rdice()
		return jsonify({"you rolled" : value}) ,200
	if (request.method == "POST"):
		return jsonify({"ErrorCode":"MISSING_INPUT_PARAMETER","Description":"JSON Error"}), 400

@app.route("/coin", methods = ["GET","POST"])
def coin():
	if (request.method=="GET"):
		out = rcoin()
		return jsonify({"you got" : out}),200
	if (request.method == "POST"):
		return jsonify({"ErrorCode":"MISSING_INPUT_PARAMETER","Description":"JSON Error"}), 400


if __name__ == "__main__":
 	app.run(debug==True)
