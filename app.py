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
  #Ruta de la página tienda con los controladores
@app.route('/tienda')
def tienda():
    return render_template('tienda.html')

  #Ruta de la página tienda con los controladores
@app.route('/Admin')
def Admin():
    return render_template('Admin.html')
#Reinialice automaticamente
if __name__ == '__main__':
    app.run(debug=True)

