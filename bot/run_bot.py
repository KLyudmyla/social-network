from faker import Faker

from bot import config
import requests
from django.http import HttpResponse
import json
import random
import logging

from bot.utils import request

logger = logging.getLogger(__name__)

fake = Faker()


def run_bot():
    number_of_users = config.NUMBER_OF_USERS

    for i in range(0, number_of_users):
        [username, password] = register_user()
        token = get_token(username, password)
        create_posts(token)
        like_post(token)
    return {"status": "OK"}


def register_user():
    username = fake.first_name()
    password = fake.password()
    email = fake.email()
    payload = json.dumps({'username': username, 'email': email, 'password': password})
    result = request(resource='users/account/register', method="POST", data=payload)
    logger.info('New user was registered. Username: %s' % username)
    if result.status_code == 201:
        return [username, password]
    else:
        logger.error('There is some problem with user signup!')
        raise Exception


def get_token(username: str, password: str):
    payload = json.dumps({'username': username, 'password': password})
    result = request(resource='api/token/', method="POST", data=payload)
    logger.debug('Token was generated for user: %s' % username)
    if result.status_code == 200:
        return json.loads(result.text)['access']
    else:
        logger.error('There is some problem with token creating')
        raise Exception


def create_posts(token: str):
    number_posts_per_user = random.randint(1, config.MAX_POSTS_PER_USER)
    try:
        for i in range(0, number_posts_per_user):
            title = fake.sentence()
            text = fake.text()
            payload = json.dumps({'title': title, 'author': None, 'text': text})
            request(resource='posts/', method="POST", data=payload, token=token)
            logger.info('New post was created: %s' % title)
    except Exception:
        logger.error('There is some problem with post sending')


def like_post(token: str):
    number_likes_per_user = random.randint(1, config.MAX_LIKES_PER_USER)
    try:
        posts = request(resource='posts', method="GET")
        post_list = [post["id"] for post in json.loads(posts.text)["results"]]
        like = 1
        for i in range(0, number_likes_per_user):
            post_id = random.choice(post_list)
            payload = json.dumps({'post': post_id, 'like': like})
            request(resource='likes/', method="POST", data=payload, token=token)
            logger.info('User like post %s' % post_id)
    except Exception:
        logger.warning('There is some problem with post sending')


run_bot()
