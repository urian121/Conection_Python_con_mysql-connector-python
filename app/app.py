from flask import Flask, render_template
import mysql.connector


app = Flask(__name__)


@app.route("/")
def index():
    mydb = mysql.connector.connect(
        host ="localhost",
        user ="root",
        passwd ="",
        database = "library_iberonex"
        )

    if mydb:
        cursor = mydb.cursor(dictionary=True)
        cursor.execute("select * from paises")
        records = cursor.fetchall()
        
        return render_template('index.html', data = records)
    else:
        return ("Error en la conexion a BD")



if __name__ == "__main__":
    app.run(debug=True, port=8000)