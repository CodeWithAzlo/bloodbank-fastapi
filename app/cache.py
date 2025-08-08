import redis
import json
from app.config import REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_TTL

# Connect to Redis pass here own redis server details, host and port
redis_client = redis.StrictRedis(
    host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True
)


def get_from_cache(key: str):
    data = redis_client.get(key)
    if data:
        return json.loads(data)
    return None


def set_to_cache(key: str, value, ttl=3600):
    redis_client.setex(key, ttl, json.dumps(value))
