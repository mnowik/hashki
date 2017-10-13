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
  # https://www.instagram.com/oauth/authorize/?client_id=9cf2788101df4970bb91a3a0b69dc14f&redirect_uri=http://localhost:5000/instagram/oauth/callback&response_type=code

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