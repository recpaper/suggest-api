'''
POST /api/word - Thêm 1 từ hoặc cụm từ vào Trie
DELET /api/word - Xóa 1 hoặc cụm từ khỏi Trie
GET /api/suggest?query=he - Tìm kiếm với tiền tố
'''

from flask import Blueprint
from flask_restful import Api

from resources.suggest import Suggest

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

api.add_resource(Suggest, '/suggest')