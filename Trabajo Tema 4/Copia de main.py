from pymongo import MongoClient


def main():

    # Enlazar mongod
    mongoClient = MongoClient('localhost', 27017)
    # Db

    db = mongoClient.ddsi
    # colección
    jugadores = db.jugador

    jugadores.delete_many({})
    # Mostrar solamente el nombre de todos los estudiantes de la base de datos
    for x in jugadores.find({}, {'_id': 0, 'nombre': 1}):
        print(x)

    # Añadir a la bd
    misJugadores = [{   "id_jugador": 1,
        "Nombre": "Pablo"
    },
    {   "id_jugador": 2,
        "Nombre": "Victor"
    },
    {   "id_jugador": 3,
        "Nombre": "Andres"
    },
    {   "id_jugador": 4,
        "Nombre": "Antonio"
    }]

    jugadores.insert_many(misJugadores)
    for x in jugadores.find():
         print(x['nombre'])


if __name__ == "__main__":
    main()
