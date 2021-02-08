from itsajungleoutthere.database import db

class Image(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))
	url = db.Column(db.Text)
	type = db.Column(db.Text)
	labels = db.relationship('Label', backref=db.backref('label', lazy='dynamic'))

	def __init__(self, name, url, type):
		self.name = name
		self.url = url
		self.type = type

	def __repr__(self):
		return '<Image %r>' % self.name