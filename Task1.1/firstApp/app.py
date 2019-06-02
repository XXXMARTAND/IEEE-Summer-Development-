from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)
api = restful.Api(app)

@app.route('/')
def intro():
    return render_template('index1.html')

@app.route('/randomDice')
def randomDice():
    randomDice = random.randint(1, 6)
    return jsonify(rolls=randomDice)

@app.route('/coinToss')
def coinToss():
    rand = random.randint(1, 2)
    coinToss = "HEADS" if rand == 1 else "TAILS"
    return jsonify(Toss=coinToss)

@app.route('/randomChance', methods=["POST"])
def randomChance():
    f = open("chances.txt", "a")
    name = request.form.get('name')
    f.write(name);
    f.close()
    if name:
        return render_template("randomAdder.html")
    f = open("chances.txt", "r") 
    newList = [i for i in f.readlines()]
    rand = random.randint(0, len(newList) - 1)
    return jsonify(Random=newList[rand])
  


