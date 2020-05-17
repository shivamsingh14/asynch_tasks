from django_redis import get_redis_connection

from doubtnut.app_logger import AppLogger

from datetime import datetime

logger = AppLogger(tag="Utils")

import datetime, json

redis = get_redis_connection()

class DateTimeUtils():

    @staticmethod
    def get_current_datetime():
        return datetime.datetime.now()

    @staticmethod
    def add_minutes_to_datetime(dt, minutes):
	    return dt + datetime.timedelta(minutes=minutes)

class RedisUtils():

    @staticmethod
    def key_exists(key):
        return redis.exists(key)

    @staticmethod
    def set_cache(key, value, ttl):
        redis.set(key, value, ttl)

    @staticmethod
    def get_cache(key):
        value = redis.get(key)
        return value if value else None

    @staticmethod
    def delete_cache(key):
        redis.delete(key)

    @staticmethod
    def insert_list(key, value):
        redis.lpush(key, value)

    @staticmethod
    def get_from_list(key, start, end):
        redis.lrange(key, start, end)

    @staticmethod
    def set_cache_with_ttl(key, ttl, value):
        logger.info("set cache, key:{}, value:{}, ttl:{}".format(key, value, ttl))
        response = redis.setex(key, ttl, value)
        return response

class JsonUtils():

    @staticmethod
    def convert_to_json(d):
        return json.dumps(d)

    @staticmethod
    def convert_to_dict(js):
        return json.loads(js)

class CONSTANTS:

    CELERY_TIMEOUT = 300 # in seconds

class Config:

    class GENERIC:

        BAD_REQUEST = "Data is required"
        EMAIL_ID_REQUIRED = "Email id is required"
        QUESTIONS_LIST = "List of questions is required"
