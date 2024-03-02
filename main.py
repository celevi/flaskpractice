from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug='true') #as changing flask app, don't need to restart website every time
