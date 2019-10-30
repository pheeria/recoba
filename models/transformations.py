from user_agents import parse
def transform(req):
    try:
        useragent = parse(req["user_agent"])
    except:
        useragent = None
    friendly_useragent = 'web'
    if useragent and useragent.is_mobile and useragent.os.family == 'iOs':
        friendly_useragent = 'apple'
    if useragent and useragent.is_mobile and useragent.os.family == 'Android':
        friendly_useragent = 'android'
    return {
        "brand": req['brand'],
        "location": {
            "lng": req["customer"]["lat"],
            "lat": req["customer"]["lon"]
        },
        "count": len(req["swimlanes"]),
        "platform": friendly_useragent,
        "originalObj": req
    }