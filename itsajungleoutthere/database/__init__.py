from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def reset_database():
	from itsajungleoutthere.database.models.image import Image			#noqa
	from itsajungleoutthere.database.models.tag import Tag				#noqa
	from itsajungleoutthere.database.models.dataset import Dataset		#noqa
	from itsajungleoutthere.database.models.label import Label			#noqa
	db.drop_all()
	db.create_all()
