import logging

from flask import request
from flask_restplus import Resource
from itsajungleoutthere.api.controllers.tag import create_tag, update_tag, delete_tag
from itsajungleoutthere.api.serializers import tag
from itsajungleoutthere.api.restplus import api
from itsajungleoutthere.database.models.tag import Tag

log = logging.getLogger(__name__)

ns = api.namespace('tags', description='Operations related to tags')


@ns.route('/')
class ImageCollection(Resource):

	@api.marshal_list_with(tag)
	def get(self):
		"""
		Returns list of tags.
		"""
		categories = Tag.query.all()
		return categories

	@api.response(201, 'Tag successfully created.')
	@api.expect(tag)
	def post(self):
		"""
		Creates a new tag.
		"""
		data = request.json
		create_tag(data)
		return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Tag not found.')
class ImageItem(Resource):

	@api.marshal_with(tag)
	def get(self, id):
		"""
		Returns a tag with a list of posts.
		"""
		return Tag.query.filter(Tag.id == id).one()

	@api.expect(tag)
	@api.response(204, 'Tag successfully updated.')
	def put(self, id):
		"""
		Updates a tag.

		* Send a JSON object with the new name in the request body.

		```
		{
		"name": "New Tag Name"
		}
		```

		* Specify the ID of the tag to modify in the request URL path.
		"""
		data = request.json
		update_tag(id, data)
		return None, 204

	@api.response(204, 'Tag successfully deleted.')
	def delete(self, id):
		"""
		Deletes tag.
		"""
		delete_tag(id)
		return None, 204
