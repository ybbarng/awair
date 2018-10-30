from awair.utils import str_to_datetime


class User:
    def __init__(self, json):
        self.user_id = json['id'] # int
        self.email = json['email'] # str
        self.first_name = json['firstName'] # str
        self.last_name = json['lastName'] # str
        self.dob_year = json['dobYear'] # int or None
        self.dob_month = json['dobMonth'] # int or None
        self.dob_day = json['dobDay'] # int or None
        self.gender = json['gender'] # str 'male', 'female'


class Device:
    def __init__(self, json):
        self.device_type = json['type'] # str 'awair-mint'
        self.device_id = json['id'] # int
        self.name = json['name'] # str
        self.space_type = json['space_type'] # str 'BEDROOM'
        self.score = Score(json['score'])
        self.preference = json['preference'] # str 'general', 'allergy', 'baby'
        self.ownership = json['ownership'] # str 'admin'


class Index:
    def __init__(self, json):
        self.temp = json['temp'] # 0
        self.humidity = json['humid'] # 1
        self.voc = json['voc'] # 1
        self.pm25 = json['pm25'] # 0


class Sensor:
    def __init__(self, json):
        self.temp = json['temp'] # 25.53
        self.humidity = json['humid'] # 38.01
        self.voc = json['voc'] # 521
        self.pm10 = json['pm10'] # 1
        self.pm25 = json['pm25'] # 0


class Meta:
    def __init__(self, json):
        self.temp = json['temp'] # 'high'
        self.humidity = json['humid'] # 'low'


class Score:
    def __init__(self, json):
        self.timestamp = str_to_datetime(json['timestamp'])
        print(self.timestamp)
        self.score = json['score']
        self.color = json['color']
        self.index = Index(json['index'])
        self.sensor = Sensor(json['sensor'])
        self.meta = Meta(json['meta'])


class Timeline:
    def __init__(self, json):
        self.timestamp = str_to_datetime(json['timestamp'])
        self.score = json['score']
        self.index = Index(json['index'])
        self.sensor = Sensor(json['sensor'])


class InboxItem:
    def __init__(self, json):
        self.title = json['title'] # str '온도', '화학물질'
        self.description = json['description'] # str
        self.icon_url = json['icon_url'] # str
        self.timestamp = str_to_datetime(json['timestamp']) # str '2018-10-25T00:25:00.000Z'
        self.link = json['link'] # str
        self.device_name = json['device_name'] # str
