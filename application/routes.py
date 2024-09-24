from application import app


@app.route('/')
def index():
    return "<h1>Hi there !!!!</h1>"