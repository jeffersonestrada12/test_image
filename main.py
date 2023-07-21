
from flask import Flask
import time


def main():
    print('Hola mundo')
    time.sleep(10)
        
if __name__ == "__main__":
    app = Flask(__name__)
    @app.route('/')
    def index():
        main()  
        return 'Procesamiento completado version PRUEBA CON NICO'  

    app.run(host='0.0.0.0', port=8080)