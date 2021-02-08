from itsajungleoutthere.database import db

class Label(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tags = db.relationship('Tag', backref=db.backref('tags', lazy='dynamic'))

    def __init__(self, tags):
        self.tags = tags

    def __repr__(self):
        return '<Label %r>' % self.tags