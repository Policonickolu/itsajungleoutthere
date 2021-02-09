from itsajungleoutthere.database import db
from itsajungleoutthere.database.models.image import Image
from itsajungleoutthere.database.models.tag import Tag

def create_image(data):
	name = data.get('name')
	url = data.get('url')
	type = data.get('type')
	image = Image(name, url, type)
	db.session.add(image)
	db.session.commit()

def update_image(image_id, data):
	image = Image.query.filter(Image.id == image_id).one()
	image.name = data.get('name')
	image.url = data.get('url')
	image.type = data.get('type')
	db.session.add(image)
	db.session.commit()

def delete_image(image_id):
	image = Image.query.filter(Image.id == image_id).one()
	db.session.delete(image)
	db.session.commit()


def add_tag_to_image(image_id, tag_id):
	image = Image.query.filter(Image.id == image_id).one()
	tag = Tag.query.filter(Tag.id == tag_id).one()
	image.tags.append(tag)
	db.session.commit()
