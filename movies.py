from settings import *
import json

db = SQLAlchemy(app)

# the class Movie will inherit the db.Model of SQLAlchemy
class Movie(db.Model):
    __tablename__ = 'movies'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    title = db.Column(db.String(80), nullable=False)
    # nullable is false so the column can't be empty
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(80), nullable=False)

    def json(self):
        return {'id': self.id, 'title': self.title,
                'year': self.year, 'genre': self.genre}
        # this method we are defining will convert our output to json

    def add_movie(_title, _year, _genre):
        # creating an instance of our Movie constructor
        new_movie = Movie(title=_title, year=_year, genre=_genre)
        db.session.add(new_movie)  # add new movie to database session
        db.session.commit()  # commit changes to session

    def get_all_movies():
        return [Movie.json(movie) for movie in Movie.query.all()]

    def get_movie(_id):
        return [Movie.json(Movie.query.filter_by(id=_id).first())]

    def update_movie(_id, _title, _year, _genre):
        movie_to_update = Movie.query.filter_by(id=_id).first()
        movie_to_update.title = _title
        movie_to_update.year = _year
        movie_to_update.genre = _genre
        db.session.commit()

    def delete_movie(_id):
        Movie.query.filter_by(id=_id).delete()
        # filter movie by id and delete
        db.session.commit()  # commiting the new change to our database