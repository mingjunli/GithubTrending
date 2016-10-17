from flask import Flask
from views.github import github_view

app = Flask(__name__)
app.register_blueprint(github_view, url_prefix="/api/github")


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
