from flask import Flask, render_template
from NW_config import buscar_noticias

app = Flask(__name__)

@app.route('/')
def index():
    noticias = buscar_noticias()
    return render_template('index.html', articles=noticias)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    
