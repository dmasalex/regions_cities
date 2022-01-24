from app import db, app
from flask_migrate import Migrate
import view


migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(debug=True)