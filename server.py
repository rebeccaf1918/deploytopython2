from flask import Flask, jsonify, url_for, request, redirect, abort
from songDAO import SongDAO
import mysql
import mysql.connector
import dbconfig as cfg

app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/')
def index():
    return "Hello World"


@app.route('/TaylorSwiftSongs', methods=['GET']) #Defining route to retieve all Taylor Swift songs from the database
def getAll():
   # converts the result from the database to a JSON format
    return jsonify(SongDAO.getAll())



@app.route('/TaylorSwiftSongs/<int:id>', methods=['GET'])
def findByID(id):
    foundSong = SongDAO.findByID(id)
    return jsonify(foundSong)


@app.route('/TaylorSwiftSongs', methods=['POST'])                                
def create():
    if not request.json:                     # Checking if the request has JSON data
        abort(400)                           # Error handling if no JSON data 
    
    SONG = {                                                           
        "Title": request.json['Title'],
        "Album": request.json['Album'],
        "Genre": request.json['Genre'],
        "Charting": request.json['Charting'],
    }
    songAdded = SongDAO.create(SONG)                # TODO ????????????????                   
    return jsonify(songAdded), 201 # creating status code


@app.route('/TaylorSwiftSongs/<int:id>', methods=['PUT'])                    
def update(id):
    foundSong = SongDAO.findByID(id)
    if not foundSong:                  # Error handling if invalid id entered
        abort(404)
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'Charting' in reqJson and type(reqJson['Charting']) is not int:    # error if charting is not an integer
        abort(400)

    if 'Title' in reqJson:
        foundSong['Title'] = reqJson['Title']
    if 'Album' in reqJson:
        foundSong['Album'] = reqJson['Album']
    if 'Genre' in reqJson:
        foundSong['Genre'] = reqJson['Genre']
    if 'Charting' in reqJson:
        foundSong['Charting'] = reqJson['Charting']
    SongDAO.update(id,foundSong)
    return jsonify(foundSong)


    
@app.route('/TaylorSwiftSongs/<int:id>' , methods=['DELETE'])
def delete(id):
    SongDAO.delete(id)
    return jsonify({"Delete complete":True})

@app.route('/findbyGenre')
def findByGenre():
    Genre= request.args.get('Genre')
    GenreType = SongDAO.findByGenre(Genre)

    if GenreType is None:
        return jsonify({"error": "No genre found."}), 404
    return jsonify(GenreType)


if __name__ == "__main__":
    app.run(debug=True)
