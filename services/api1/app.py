from flask import request, Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from redis import Redis

from config import configure_app
from model import db, User

#######################
#### configuration ####
#######################
app = Flask(__name__)
configure_app(app)

# db
db.init_app(app)

# redis
redis = Redis(host='redis', port=app.config['REDIS_PORT'])


#############
#### APP ####
#############
@app.route('/')
def hello():
    user = User.query.first()
    count = redis.incr('hits')
    return user.username


@app.route('/retrieve/<string:hashtag>')
def fetch_pictures(hashtag):
  return hashtag


@app.route('/instagram/oauth/callback')
def handle_callback():
  if request.method == 'POST':
    return "test"
  return "request"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)