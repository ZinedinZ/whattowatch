from flask import Flask, render_template, request
from findmovie import FindMovie as Fm

app = Flask(__name__)


@app.route("/")
def ui():
    # Create a home page and ui
    return render_template("base.html")


@app.route("/movies", methods=["POST"])
def movies():
    # Takes user input and return genre id
    genre = request.form.get("genre")
    genre_id = str(Fm().find_genres(genre))

    data = Fm().find_movie(genre_id)
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
