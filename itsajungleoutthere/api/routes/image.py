import logging

from flask import request
from flask_restplus import Resource
from itsajungleoutthere.api.controllers.image import create_image, update_image, delete_image
from itsajungleoutthere.api.serializers import image
from itsajungleoutthere.api.restplus import api
from itsajungleoutthere.database.models.image import Image

log = logging.getLogger(__name__)

ns = api.namespace('images', description='Operations related to images')


@ns.route('/')
class ImageCollection(Resource):

	@api.marshal_list_with(image)
	def get(self):
		"""
		Returns list of images.
		"""
		categories = Image.query.all()
		return categories

	@api.response(201, 'Image successfully created.')
	@api.expect(image)
	def post(self):
		"""
		Creates a new image.
		"""
		data = request.json
		create_image(data)
		return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Image not found.')
class ImageItem(Resource):

	@api.marshal_with(image)
	def get(self, id):
		"""
		Returns a image with a list of posts.
		"""
		return Image.query.filter(Image.id == id).one()

	@api.expect(image)
	@api.response(204, 'Image successfully updated.')
	def put(self, id):
		"""
		Updates a image.

		* Send a JSON object with the new name in the request body.

		```
		{
		"name": "New Image Name"
		}
		```

		* Specify the ID of the image to modify in the request URL path.
		"""
		data = request.json
		update_image(id, data)
		return None, 204

	@api.response(204, 'Image successfully deleted.')
	def delete(self, id):
		"""
		Deletes image.
		"""
		delete_image(id)
		return None, 204
