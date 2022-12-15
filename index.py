from app import app
from Database.db import db


db.init_app(app)
with app.app_context():
    db.create_all()


if __name__ == "__main__":

    app.run(
        debug=True,
        port=8000
    )


