from user_agents import parse
def transform(req):
    useragent = parse(req["user_agent"])
    friendly_useragent = 'web'
    if useragent.is_mobile and useragent.os.family == 'iOs':
        friendly_useragent = 'apple'
    if useragent.is_mobile and useragent.os.family == 'Android':
        friendly_useragent = 'android'
    return {
        "brand": req['brand'],
        "location": {
            "lat": req["customer"]["lat"],
            "lng": req["customer"]["lon"]
        },
        "count": len(req["swimlanes"]),
        "platform": friendly_useragent
    }