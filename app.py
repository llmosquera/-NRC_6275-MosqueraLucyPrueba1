#importar la libreria flask
from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder='templates')
 
#Para reproducir automaticamente 
if __name__ == "__main__":
	app.run(debug=True)
 
 
 #Ruta de la página principal con los controladores
 
@app.route('/')
def index():
    return render_template('index.html')
 #Iniciamos la aplicacion

if __name__ == '__main__':
    app.run(debug=True)

