import express from 'express'
import mongoose from 'mongoose'
import { get_genres, get_genre } from './controllers/api_get.js'


//Crea app y define el puerto del servidor.
const app = express()
const PORT = 3000

//Conexion a la base de datos.
mongoose
    .connect('mongodb://127.0.0.1:27017/music')
    .then(()=>console.log('Conectado a la base de datos.'))
    .catch(()=>console.log('Error'))

//Endpoints
get_genres(app)
get_genre(app)


//Monta el servidor.
app.listen(PORT, ()=>console.log(`Servidor en http://localhost:${PORT}`))



