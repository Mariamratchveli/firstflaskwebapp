from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy
# import os
# os.system("pip install Flask-SQLAlchemy")




app = Flask(__name__)
app.config['SECRET_KEY'] = 'pythonwork'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.sqlite'
db = SQLAlchemy(app)

class movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    direcor = db.Column(db.String(40), nullable=False)
    year = db.Column(db.Float, nullable=False)

    def __str__(self):
        return f'movie title:{self.title}; Director: {self.author}; Release: {self.year}'




@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/mypage')
def mypage():

    movies = ['Movie 1', 'Movie 2', 'Movie 3']
    return render_template('mypage.html', movies=movies)



@app.route('/movies')
def addmovies():
    return render_template('addmovies.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')



# @app.route('/movies', methods=['GET', 'POST'])
# def movies():
#     if request.method == 'POST':
#         t = request.form['title']
#         d = request.form['director']
#         y = request.form['Release year']
#         return 'Movie added successfully!'
#     return render_template('mypage.html')
@app.route('/movies', methods=['GET', 'POST'])
def movies():
    if request.method == 'POST':
        title = request.form['title']
        director = request.form['director']
        y = request.form['Release year']

        if not title or not director:
            flash('Please fill out all fields.', 'error')
        else:
            movie = movies(title=title, director=director)
            db.session.add(movie)
            db.session.commit()
            flash('Movie added successfully!', 'success')
    return render_template('addmovies.html', movies=movies)



if __name__ == '__main__':
    app.run(debug=True)
