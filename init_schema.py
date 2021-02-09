from itsajungleoutthere.app import initialize_app, app
from itsajungleoutthere.database import reset_database

initialize_app(app)
with app.app_context():
	reset_database()