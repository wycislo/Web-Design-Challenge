from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [

    {
        'author': 'Henry',
        'title': 'DBA',
    }
]



@app.route("/")
def home():
    return render_template('home.html', posts=posts, title='Home')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)