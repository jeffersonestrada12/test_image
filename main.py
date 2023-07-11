
from flask import Flask



def main():
    print('Hola mundo')
        

if __name__ == "__main__":
    app = Flask(__name__)
    @app.route('/')
    def index():
        main()  
        return 'Procesamiento completado'  

    app.run(host='0.0.0.0', port=8080)