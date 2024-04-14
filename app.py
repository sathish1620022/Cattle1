from flask import Flask
from view import view

app=Flask(__name__)
app.secret_key="qwas"
app.register_blueprint(view,url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True)