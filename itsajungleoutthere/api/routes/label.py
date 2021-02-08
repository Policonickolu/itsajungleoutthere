import logging

from flask import request
from flask_restplus import Resource
from itsajungleoutthere.api.controllers.label import create_label, update_label, delete_label
from itsajungleoutthere.api.serializers import label
from itsajungleoutthere.api.restplus import api
from itsajungleoutthere.database.models.label import Label

log = logging.getLogger(__name__)

ns = api.namespace('labels', description='Operations related to labels')


@ns.route('/')
class ImageCollection(Resource):

	@api.marshal_list_with(label)
	def get(self):
		"""
		Returns list of labels.
		"""
		categories = Label.query.all()
		return categories

	@api.response(201, 'Label successfully created.')
	@api.expect(label)
	def post(self):
		"""
		Creates a new label.
		"""
		data = request.json
		create_label(data)
		return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Label not found.')
class ImageItem(Resource):

	@api.marshal_with(label)
	def get(self, id):
		"""
		Returns a label with a list of posts.
		"""
		return Label.query.filter(Label.id == id).one()

	@api.expect(label)
	@api.response(204, 'Label successfully updated.')
	def put(self, id):
		"""
		Updates a label.

		* Send a JSON object with the new name in the request body.

		```
		{
		"name": "New Label Name"
		}
		```

		* Specify the ID of the label to modify in the request URL path.
		"""
		data = request.json
		update_label(id, data)
		return None, 204

	@api.response(204, 'Label successfully deleted.')
	def delete(self, id):
		"""
		Deletes label.
		"""
		delete_label(id)
		return None, 204
