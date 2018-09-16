from flask import request
from flask_restful import Resource
from redis_client import client

from trie import insertCompletion

class Suggest(Resource):
  def get(self):
    query = request.args.get('query')
    data = client.zrange(query, 0, 5, desc=True, withscores=False)
    print(query)
    return {
      'status': 'success',
      'data': data
    }, 200
  
  def post(self):
    json_data = request.get_json(force=True)
    if not json_data:
      return {
        'message': 'No input data'
      }, 400
    
    insert = insertCompletion(json_data['data'], json_data['score'])
    if insert == 'ok':
      return {
        'status': 'success',
        'message': 'add success'
      }, 200
    
    return {
      'message': 'null'
    }, 400