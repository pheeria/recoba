from user_agents import parse


def transform(req):
    try:
        useragent = parse(req["user_agent"])
    except:
        useragent = None
    friendly_useragent = "web"
    if useragent and useragent.is_mobile and useragent.os.family == "iOS":
        friendly_useragent = "apple"
    if useragent and useragent.is_mobile and useragent.os.family == "Android":
        friendly_useragent = "android"
    if useragent == "android":
        friendly_useragent = "android"

    return {
        "id": req["request_id"],
        "brand": req["brand"],
        "location": {
            "lng": req["customer"]["lat"],
            "lat": req["customer"]["lon"]
        },
        "count": len([s for s in req["swimlanes"] if len(s["restaurant_ids"]) > 0]),
        "total": len(req["swimlanes"]),
        "platform": friendly_useragent,
        "original": req
    }
