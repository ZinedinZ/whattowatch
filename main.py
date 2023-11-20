from flask import Flask, render_template, request
from findmovie import FindMovie as fm

app = Flask(__name__)

@app.route("/")
def ui():
    return render_template("base.html")

@app.route("/movie", methods=["POST"])
def movie():
    genre = request.form.get("genre")
    genre_id = str(fm().find_genres(genre))
    data = fm().find_movie(genre_id)
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)


