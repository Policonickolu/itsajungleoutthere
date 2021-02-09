from itsajungleoutthere.database import db
from itsajungleoutthere.database.models.dataset import Dataset

def create_dataset(data):
	name = data.get('name')
	images = data.get('images')
	dataset = Dataset(name)
	db.session.add(dataset)
	db.session.commit()

def update_dataset(dataset_id, data):
	dataset = Dataset.query.filter(Dataset.id == dataset_id).one()
	dataset.name = data.get('name')
	db.session.add(dataset)
	db.session.commit()

def delete_dataset(dataset_id):
	dataset = Dataset.query.filter(Dataset.id == dataset_id).one()
	db.session.delete(dataset)
	db.session.commit()
