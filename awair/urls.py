class AwairUrls:
    login = 'https://mobile-app.awair.is/v1/users/login'
    get_user = 'https://mobile-app.awair.is/v1/users/self'
    get_devices = 'https://internal.awair.is/v1.1/users/self/devices'
    get_score = 'https://internal.awair.is/v1/devices/{device_type}/{device_id}/events/score?desc=true&limit=1'
    get_timelines = 'https://internal.awair.is/v1.2/devices/{device_type}/{device_id}/timeline'
    get_inbox_items = 'https://internal.awair.is/v1/users/self/inbox-items'
