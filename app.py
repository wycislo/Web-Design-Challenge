from flask import Flask, render_template, url_for, send_from_directory

app = Flask(__name__, static_url_path= '/')

@app.route("/")
def index():
    return 'index.html'

if __name__ == '__main__':
    app.run(debug=True)