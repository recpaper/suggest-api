from flask import Flask
from flask_cors import CORS

def create_app(config_filename):
  app = Flask(__name__)
  CORS(app)
  # app.config.from_object(config_filename)

  from app import api_blueprint

  app.register_blueprint(api_blueprint, url_prefix='/api')

  return app

if __name__ == '__main__':
  app = create_app("config")
  app.run(host='0.0.0.0', port=5000)

