from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def intro():
    return render_template('index1.html')

@app.route('/randomDice')
def randomDice():
    randomDice = random.randint(1, 6)
    return render_template("randomDice.html", randomDice=randomDice)

@app.route('/coinToss')
def coinToss():
    rand = random.randint(1, 2)
    coinToss = "HEADS" if rand == 1 else "TAILS"
    return render_template("coinToss.html", coinToss=coinToss)

@app.route('/randomChance', methods=["POST"])
def randomChance():
    return render_template("failure.html")
