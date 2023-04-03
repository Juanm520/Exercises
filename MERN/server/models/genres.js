import mongoose from 'mongoose'

const musicGenresSchema = mongoose.Schema({
    genre: {
        title: String,
        subgenre: Array,
    },
})

export const Genres = mongoose.model('genre', musicGenresSchema)

