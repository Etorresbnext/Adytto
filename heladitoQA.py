from waitress import serve
from Automatizaditto_WebProject.Backend.heladito import heladito

if __name__ == '__main__':
    serve(heladito, host="0.0.0.0", port=5000)
