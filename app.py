from flask import Flask, Blueprint
from session_act.__init__ import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)