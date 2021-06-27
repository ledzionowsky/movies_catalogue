from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def homepage():
    movies = ['skazani na shawshank', "zielona mila"]
    print("asxksdmcjdcj")
    return render_template("homepage.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)