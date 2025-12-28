from flask import Flask, jsonify
import os

app = Flask(__name__)



class Link:
    def __init__(self, movieId, imdbId, tmdbId):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId

class Rating:
    def __init__(self, userId, movieId, rating, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp

class Tag:
    def __init__(self, userId, movieId, tag, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp


def get_data(filename, model_class):
    results = []
    path = os.path.join('Python_api', f'{filename}.csv')
    
    if not os.path.exists(path):
        return {"error": f"File {filename}.csv not found"}

    with open(path, 'r', encoding='utf-8') as file:
        next(file) 
        for line in file:
            parts = line.strip().split(',')
            
            obj = model_class(*parts)
            results.append(obj.__dict__)
    return results



@app.route('/links')
def links_endpoint():
    return jsonify(get_data('links', Link))

@app.route('/ratings')
def ratings_endpoint():
    return jsonify(get_data('ratings', Rating))

@app.route('/tags')
def tags_endpoint():
    return jsonify(get_data('tags', Tag))

if __name__ == '__main__':
    app.run(debug=True)