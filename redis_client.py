import redis
import config

client = redis.StrictRedis(
    host='redis', port=6379, db=1, decode_responses=True)