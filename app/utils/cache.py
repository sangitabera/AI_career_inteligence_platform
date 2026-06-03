import json
from app.core.redis_client import redis_client

def get_cache(key):
    try:
        value = redis_client.get(key)
        return json.loads(value) if value else None
    except Exception as e:
        print(f"Redis Error: {e}")
        return None


def set_cache(key, value, expiry=3600):
    try:
        redis_client.setex(
            key,
            expiry,
            json.dumps(value)
        )
    except Exception as e:
        print(f"Redis Error: {e}")