import logging

from flask import request
from flask_restplus import Resource
from itsajungleoutthere.api.controllers.tag import create_tag, update_tag, delete_tag
from itsajungleoutthere.api.serializers import tag, image
from itsajungleoutthere.api.restplus import api
from itsajungleoutthere.database.models.tag import Tag
from itsajungleoutthere.database.models.image import Image
from itsajungleoutthere.api.parsers import pagination_arguments

log = logging.getLogger(__name__)

ns = api.namespace('tags', description='Operations related to tags')


@ns.route('/')
class TagCollection(Resource):

	@api.marshal_list_with(tag)
	def get(self):
		tags = Tag.query.all()
		return tags

	@api.response(201, 'Tag successfully created.')
	@api.expect(tag)
	def post(self):
		data = request.json
		create_tag(data)
		return None, 201


@ns.route('/<int:id>/images')
class TagImageCollection(Resource):
	
	@api.expect(pagination_arguments)
	@api.marshal_list_with(image)
	def get(self, id):

		args = pagination_arguments.parse_args(request)
		page = args.get('page', 1)
		per_page = args.get('per_page', 10)

		images_query = Image.query
		images = images_query.join(Image.tags).filter(Tag.id == id).paginate(page, per_page, error_out=False)
		return images.items

@ns.route('/<int:id>')
@api.response(404, 'Tag not found.')
class TagItem(Resource):

	@api.marshal_with(tag)
	def get(self, id):
		return Tag.query.filter(Tag.id == id).one()

	@api.expect(tag)
	@api.response(204, 'Tag successfully updated.')
	def put(self, id):

		data = request.json
		update_tag(id, data)
		return None, 204

	@api.response(204, 'Tag successfully deleted.')
	def delete(self, id):
		delete_tag(id)
		return None, 204
