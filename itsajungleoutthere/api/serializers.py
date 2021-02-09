from flask_restplus import fields
from itsajungleoutthere.api.restplus import api

tag = api.model('Tag', {
	'id': fields.Integer(readOnly=True, description='The unique identifier of a tag'),
	'name': fields.String(required=True, description='Tag name')
})

# label = api.model('Labeling with tags', {
# 	'id': fields.Integer(readOnly=True, description='The unique identifier of a label'),
# 	'tags': fields.List(fields.Nested(tag))
# })

image = api.model('Image', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of an image'),
    'name': fields.String(required=True, description='Image name'),
    'url': fields.String(required=True, description='Image url'),
    'type': fields.String(required=True, description='Image type'),
})

# dataset = api.model('Dataset of images', {
# 	'id': fields.Integer(readOnly=True, description='The unique identifier of a dataset'),
# 	'name': fields.String(required=True, description='Dataset name'),
# })