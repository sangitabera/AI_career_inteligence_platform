import redis
import os

REDIS_HOST = os.getenv(
    "REDIS_HOST",
    "localhost"
)

redis_client = redis.Redis(
    host = 'localhost',
    port = 6379,
    decode_responses = True,
    socket_connect_timeout=2
)