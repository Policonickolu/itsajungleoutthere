from itsajungleoutthere.database import db

label_tag_association_table = db.Table('label_tag_association', db.Model.metadata,
    db.Column('label_id', db.Integer, db.ForeignKey('label.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)

class Label(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	image_id = db.Column(db.Integer, db.ForeignKey('image.id'), nullable=False)
	tags = db.relationship('Tag', secondary=label_tag_association_table, lazy='subquery',
		backref=db.backref('label', lazy=True))

	def __init__(self, image_id):
		self.image_id = image_id

	def __repr__(self):
		return '<Label %r>' % self.tags