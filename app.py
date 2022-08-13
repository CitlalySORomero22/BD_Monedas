import web
import pymongo

urls = (

    '/', 'index' 
)

conexion = pymongo.MongoClient("mongodb+srv://citlaly:bd2210@monedas.4ln7qvy.mongodb.net/?retryWrites=true&w=majority")
db = conexion.Monedas

class index:

    def GET(self):
        Moneda = db.tipo_moneda
        monedas = Moneda.find()
        return monedas

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()