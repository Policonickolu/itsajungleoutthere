from itsajungleoutthere.database import db

image_tag_association_table = db.Table('image_tag_association', db.Model.metadata,
	db.Column('image_id', db.Integer, db.ForeignKey('image.id'), primary_key=True),
	db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)

class Image(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))
	url = db.Column(db.Text)
	type = db.Column(db.Text)
	tags = db.relationship('Tag', secondary=image_tag_association_table, lazy='subquery',
		backref=db.backref('image', lazy=True))

	def __init__(self, name, url, type):
		self.name = name
		self.url = url
		self.type = type

	def __repr__(self):
		return '<Image %r>' % self.name