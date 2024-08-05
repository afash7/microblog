from app import app 


@app.route('/')
@app.route('/index')
def index():
    return "micro blog Flask App"