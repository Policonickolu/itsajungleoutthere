from itsajungleoutthere.database import db

class Dataset(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))
	images = db.relationship('Image', backref=db.backref('images', lazy='dynamic'))

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return '<Dataset %r>' % self.name