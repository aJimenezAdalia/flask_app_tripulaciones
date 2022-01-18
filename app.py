import psycopg2
import pandas as pd
from flask import Flask

# Conexión a la BBDD de AWS
conexion = psycopg2.connect(
    host="ec2-3-232-22-121.compute-1.amazonaws.com", 
    database="d81chghjf1jua5", 
    user="zidhunkmriujqn", 
    password="87f2440a677b1f6f1b1718f7a970b9a1a9f2b27b626f8464a28c7eadad9a21b4")

# Cursor de la conexión
cursor = conexion.cursor()

# Con esta función leemos los datos y lo pasamos a un DataFrame de Pandas
def sql_query(query):

    # Ejecuta la query
    cursor.execute(query)

    # Almacena los datos de la query 
    ans = cursor.fetchall()

    # Obtenemos los nombres de las columnas de la tabla
    names = [description[0] for description in cursor.description]

    return pd.DataFrame(ans,columns=names)

# Flask App
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/api/<string:uuid>', methods=['GET'])
def get_assets(uuid):
    from web_scrap import web_scraping
    # Query con la uuid obtenida de FullStack
    query = f"""
    SELECT images, domains 
    FROM assets WHERE "userId" IN 
        (SELECT id FROM users 
        WHERE uuid = '{uuid}')"""
    # DataFrame con la información de la query
    df = sql_query(query)

    # JSON - return
    json_mostrar = web_scraping(image=df['images'][0][0], domain=df['domains'][0][0])

    return json_mostrar

app.run()