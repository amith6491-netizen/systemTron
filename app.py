from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("landingpage.html")

@app.route("/snake")
def snake_game():
    import snake
    return "Snake game executed in backend!"

if __name__ == "__main__":
    app.run(debug=True)
