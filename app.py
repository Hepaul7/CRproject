from flask import Flask, render_template
import numpy as np

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/matrix.html')
def matrix():
    interaction_matrix = np.load('interaction_matrix.npy')
    cards = [str(x) for x in range(1, 110)]
    return render_template("matrix.html", cards=cards,
                           interactions=interaction_matrix.tolist())


if __name__ == '__main__':
    app.run()
