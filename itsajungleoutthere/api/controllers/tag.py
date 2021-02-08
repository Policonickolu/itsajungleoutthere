from itsajungleoutthere.database import db
from itsajungleoutthere.database.models.tag import Tag

def create_tag(data):
	name = data.get('name')
	tag = Tag(name)
	db.session.add(tag)
	db.session.commit()

def update_tag(tag_id, data):
	tag = Tag.query.filter(Tag.id == tag_id).one()
	tag.name = data.get('name')
	db.session.add(tag)
	db.session.commit()

def delete_tag(tag_id):
	tag = Tag.query.filter(Tag.id == tag_id).one()
	db.session.delete(tag)
	db.session.commit()
