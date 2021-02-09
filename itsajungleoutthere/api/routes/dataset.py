import logging

from flask import request
from flask_restplus import Resource
from itsajungleoutthere.api.controllers.dataset import create_dataset, update_dataset, delete_dataset
from itsajungleoutthere.api.serializers import dataset
from itsajungleoutthere.api.restplus import api
from itsajungleoutthere.database.models.dataset import Dataset

log = logging.getLogger(__name__)

ns = api.namespace('datasets', description='Operations related to datasets')


@ns.route('/')
class DatasetCollection(Resource):

	@api.marshal_list_with(dataset)
	def get(self):
		datasets = Dataset.query.all()
		return datasets

	@api.response(201, 'Dataset successfully created.')
	@api.expect(dataset)
	def post(self):
		data = request.json
		create_dataset(data)
		return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Dataset not found.')
class DatasetItem(Resource):

	@api.marshal_with(dataset)
	def get(self, id):
		return Dataset.query.filter(Dataset.id == id).one()

	@api.expect(dataset)
	@api.response(204, 'Dataset successfully updated.')
	def put(self, id):
		data = request.json
		update_dataset(id, data)
		return None, 204

	@api.response(204, 'Dataset successfully deleted.')
	def delete(self, id):
		delete_dataset(id)
		return None, 204
