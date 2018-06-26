from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "home.html"

@app.route('/about/')
def about():
    return "about.html"

if __name__=="__main__":
    app.run(debug=True)
