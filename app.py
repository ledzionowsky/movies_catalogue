from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = ['skazani na shawshank', "zielona mila",'ironman',"jamesbond", 'forest gump', 'pulp fiction']
    return render_template("homepage.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)