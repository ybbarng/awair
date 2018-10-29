# Awair
A python wrapper for [Awair](https://getawair.com/) private API

## Dependencies
* pytz
* requests

## How to use
```python
from datetime import datetime
from datetime import timedelta

from awair import Awair
from awair.enums import DeviceType

email = 'myId@test.com'
password = 'myStrongPassword!'
device_id = '1234'

start_dt = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
end_dt = start_dt + timedelta(days=1)

awair = Awair(email, password)
timelines = awair.get_timelines(DeviceType.AWAIR_MINT, device_id, start_dt, end_dt)
for timeline in timelines:
    print(timeline.timestamp)
    print(timeline.score)
```

## Alternatives
* https://github.com/harperreed/pyawair/blob/master/awair.py
* https://github.com/netmanchris/pyawair/tree/master/pyawair
