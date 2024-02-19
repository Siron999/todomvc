from datetime import datetime, timedelta

import jwt
from rest_framework import permissions
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed, ParseError


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # Extract the JWT from the Authorization header
        jwt_token = request.headers.get('Authorization')
        if jwt_token is None:
            raise AuthenticationFailed('Authentication token missing')

        jwt_token = JWTAuthentication.get_the_token_from_header(
            jwt_token)

        # Decode the JWT and verify its signature
        try:
            payload = jwt.decode(
                jwt_token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.exceptions.InvalidSignatureError:
            raise AuthenticationFailed('Invalid signature')
        except:
            raise ParseError()

        # Get the user from the database
        username = payload.get('username')
        if username is None:
            raise AuthenticationFailed('Username not found in JWT')

        user = User.objects.filter(username=username).first()
        if user is None:
            raise AuthenticationFailed('User not found')

        # Return the user and token payload
        return user, payload

    def authenticate_header(self, request):
        return 'Bearer'

    @staticmethod
    def create_jwt(user):
        # Create the JWT payload
        payload = {
            'exp': int((datetime.now() + timedelta(hours=settings.JWT_CONF['TOKEN_LIFETIME_HOURS'])).timestamp()),
            # set the expiration time for 5 hour from now
            'iat': datetime.now().timestamp(),
            'username': user.username
        }

        # Encode the JWT with your secret key
        jwt_token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        return jwt_token

    @staticmethod
    def get_the_token_from_header(token):
        token = token.replace('Bearer', '').replace(' ', '')
        return token


class IsCustomAdminUser(permissions.BasePermission):

    def has_permission(self, request, view):
        print(request.user.username == "sironshakya")
        return request.user.username == "sironshakya"
