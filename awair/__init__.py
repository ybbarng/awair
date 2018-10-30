from awair.auth import Auth
from awair.conn import AwairRequest
from awair.enums import *
from awair.models import *
from awair.urls import AwairUrls
from awair.utils import datetime_to_str


class Awair:
    user = None
    devices = None

    def __init__(self, email=None, password=None, access_token=None):
        auth = Auth(email, password, access_token)
        self._api = AwairRequest(auth.access_token)

    def get_user(self):
        if self.user is None:
            self.user = User(self._api.get(AwairUrls.get_user))
        return self.user

    def get_devices(self):
        if self.devices is None:
            self.devices = [Device(device) for device in self._api.get(AwairUrls.get_devices)['data']]
        return self.devices

    def get_score(self, device_type, device_id):
        return Score(self._api.get(AwairUrls.get_score.format(device_type=device_type.value, device_id=device_id))['data'][0])

    def get_timelines(self, device_type, device_id, start_dt, end_dt):
        params = {
            'from': datetime_to_str(start_dt),
            'to': datetime_to_str(end_dt)
        }
        response = self._api.get(AwairUrls.get_timelines.format(device_type=device_type.value, device_id=device_id), data=params)
        has_next = response['pagination']['has_next']
        return [Timeline(timeline) for timeline in response['data']]

    def get_inbox_items(self, start_dt, end_dt, lang):
        params = {
            'from': datetime_to_str(start_dt),
            'to': datetime_to_str(end_dt),
            'lang': lang
        }
        response = self._api.get(AwairUrls.get_inbox_items, data=params)
        has_next = response['pagination']['has_next']
        return [InboxItem(inbox_item) for inbox_item in response['data']]
