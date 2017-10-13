from flask import request, Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return 'Hello World 2! I have been seen {} times.\n'.format(count)


def build_register_url():
  return 

@app.route('/retrieve/<string:hashtag>')
def fetch_pictures(hashtag):
  return hashtag

@app.route('/instagram/oauth/callback')
def handle_callback():
  if request.method == 'POST':
    return "yolo"
  return "request"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)