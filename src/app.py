from flask import Flask
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()


@app.route('/')
def index():
    username = os.getenv('USER')
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    
    print(username, email, password)
    
    
    return '<h1>app flask desployeada en render.<br> {}<br> {} <br> {}</h1>'.format(username, email, password)


def status_404(error):
    return '<h1> Pagina no encontrada </h1>'

if __name__ == "__main__":
    app.register_error_handler(404, status_404)
    app.run()