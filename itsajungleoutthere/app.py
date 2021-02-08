import logging.config
import os
from flask import Flask, Blueprint
from itsajungleoutthere import settings
from itsajungleoutthere.api.routes.image import ns as images_namespace
from itsajungleoutthere.api.routes.tag import ns as tags_namespace
from itsajungleoutthere.api.routes.dataset import ns as datasets_namespace
from itsajungleoutthere.api.routes.label import ns as labels_namespace
from itsajungleoutthere.api.restplus import api
from itsajungleoutthere.database import db


app = Flask(__name__)
logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '../logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)

if __name__ == "__main__":

    # config

    app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP

    # init

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(images_namespace)
    api.add_namespace(tags_namespace)
    api.add_namespace(datasets_namespace)
    api.add_namespace(labels_namespace)
    app.register_blueprint(blueprint)
    db.init_app(app)

    # run

    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=settings.FLASK_DEBUG)

