import logging

from flask import request
from flask_restplus import Resource
from itsajungleoutthere.api.controllers.image import create_image, update_image, delete_image, add_tag_to_image
from itsajungleoutthere.api.serializers import image, tag
from itsajungleoutthere.api.restplus import api
from itsajungleoutthere.database.models.image import Image
from itsajungleoutthere.api.parsers import pagination_arguments


log = logging.getLogger(__name__)

ns = api.namespace('images', description='Operations related to images')


@ns.route('/')
class ImageCollection(Resource):

	@api.expect(pagination_arguments)
	@api.marshal_list_with(image)
	def get(self):
		args = pagination_arguments.parse_args(request)
		page = args.get('page', 1)
		per_page = args.get('per_page', 10)

		images_query = Image.query
		images = images_query.paginate(page, per_page, error_out=False)
		return images.items

	@api.response(201, 'Image successfully created.')
	@api.expect(image)
	def post(self):
		data = request.json
		create_image(data)
		return None, 201


@ns.route('/<int:id>/tags')
class ImageTagCollection(Resource):
	
	@api.marshal_list_with(tag)
	def get(self, id):
		return Image.query.filter(Image.id == id).one().tags


@ns.route('/<int:id>')
@api.response(404, 'Image not found.')
class ImageItem(Resource):

	@api.marshal_with(image)
	def get(self, id):
		return Image.query.filter(Image.id == id).one()

	@api.expect(image)
	@api.response(204, 'Image successfully updated.')
	def put(self, id):
		
		data = request.json
		update_image(id, data)
		return None, 204

	@api.response(204, 'Image successfully deleted.')
	def delete(self, id):
		delete_image(id)
		return None, 204

@ns.route('/<int:image_id>/tags/<int:tag_id>')
@api.response(404, 'Image or Tag not found.')
class ImageTagItem(Resource):

	@api.response(204, 'Tag successfully added to image.')
	def put(self, image_id, tag_id):

		add_tag_to_image(image_id, tag_id)
		return None, 204




