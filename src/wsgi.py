from app import create_app

flaskapp = create_app()

if __name__ == '__main__':
    flaskapp.run(host='0.0.0.0', port=8080)
