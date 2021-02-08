from itsajungleoutthere.database import db
from itsajungleoutthere.database.models.label import Label

def create_label(data):
	tags = data.get('tags')
	label = Label(tags)
	db.session.add(label)
	db.session.commit()

def update_label(label_id, data):
	label = Tag.query.filter(Label.id == label_id).one()

	db.session.add(label)
	db.session.commit()

def delete_label(label_id):
	label = Label.query.filter(Label.id == label_id).one()
	db.session.delete(label)
	db.session.commit()
