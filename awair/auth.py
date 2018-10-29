from awair.conn import AwairRequest, RequestException
from awair.urls import AwairUrls


class CredentialException(Exception):
    pass


class Auth:
    def __init__(self, email=None, password=None, access_token=None):
        if not access_token:
            if email is None or password is None:
                raise CredentialException('Please enter your email and the password.')
            access_token = self.get_access_token(email, password)
            print('Your access token: {}'.format(access_token))
        self.access_token = access_token

    def get_access_token(self, email, password):
        awairRequest = AwairRequest()
        data = {
            'email': email,
            'password': password
        }
        try:
            return awairRequest.post(AwairUrls.login, json_data=data)['accessToken']
        except RequestException as e:
            raise CredentialException('Failed to login: {}'.format(e))
