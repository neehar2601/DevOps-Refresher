from flask import Flask
from redis import Redis

app = Flask(__name__)
# MAGIC: We connect to a host named "redis".
# Docker Compose will automatically make this name work!
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return '<h1>Hello World! I have been seen {} times.</h1>'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
