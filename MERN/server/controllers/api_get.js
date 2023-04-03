import { Genres } from '../models/genres.js'

function get_genres(app){

    return app.get('/api/genres', (req, res) => {
        Genres.find()
        .then(genres => res.json(genres))
    })
}

function get_genre(app){

    return app.get('/api/genres/:genre', (req, res) => {
    const { genre } = req.params
        Genres
        .findOne({ 'genre.title' : genre })
        .then(genre => res.json(genre))
    })
}

export {get_genres, get_genre}