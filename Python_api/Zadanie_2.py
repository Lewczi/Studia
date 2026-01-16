from flask import Flask, jsonify
import os

app = Flask(__name__)

class Movie:
    def __init__(self, movieId, title, genres):
        self.movieId = movieId
        self.title = title
        self.genres = genres

def get_movies_from_file():
    movies_list = []
    file_path = os.path.join('Python_api', 'movies.csv')
    
    with open(file_path, 'r', encoding='utf-8') as file:
        next(file)
        for line in file:
            parts = line.strip().split(',', 2)
            if len(parts) == 3:
                movie_obj = Movie(parts[0], parts[1], parts[2])
                movies_list.append(movie_obj.__dict__)
                
    return movies_list

@app.route('/movies')
def movies_endpoint():
    data = get_movies_from_file()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)