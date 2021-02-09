from itsajungleoutthere.database import db

dataset_image_association_table = db.Table('dataset_image_association', db.Model.metadata,
    db.Column('dataset_id', db.Integer, db.ForeignKey('dataset.id')),
    db.Column('image_id', db.Integer, db.ForeignKey('image.id'))
)

class Dataset(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))
	images = db.relationship('Image', secondary=dataset_image_association_table)

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return '<Dataset %r>' % self.name