from flask import Flask,render_template, request
import requests
from deep_translator import GoogleTranslator
app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/clima" , methods =['POST'])
def obtenerClima():
    if request.method == 'POST':
        ciudad = request.form['ciudad']
        api_key = "06bf23d240994752989180631252207"
        url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={ciudad}&aqi=no"
        respuesta = requests.get(url)
        datos = respuesta.json()
        if respuesta.status_code == 200:
            grados = datos["current"]["temp_c"]
            humedad = datos["current"]["humidity"]
            imagen = datos["current"]["condition"]["icon"]
            descripcion = datos["current"]["condition"]["text"]
            descripcion_traducida = GoogleTranslator(source="english", target="spanish").translate(descripcion)
            viento = datos["current"]["wind_kph"]
            return render_template("index.html", humedad=humedad,ciudad=ciudad, grados=grados, imagen=imagen,descripcion = descripcion_traducida, viento = viento,mostrar_carta=True)
        else:
            return render_template("index.html", ciudad = "Ciudad no enccontrada")
if __name__ == "__main__":
    app.run(debug = True)
