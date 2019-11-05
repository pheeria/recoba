from user_agents import parse


def transform(req):
    req_agent = str(req["user_agent"]).lower()
    friendly_useragent = "web"

    if "android" in req_agent:
        friendly_useragent = "android"
    elif "ios" in req_agent:
        friendly_useragent = "apple"
    else:
        try:
            useragent = parse(req["user_agent"])
        except:
            useragent = None
        if useragent and useragent.is_mobile and useragent.os.family == "iOS":
            friendly_useragent = "apple"
        if useragent and useragent.is_mobile and useragent.os.family == "Android":
            friendly_useragent = "android"

    return {
        "id": req["request_id"],
        "brand": req["brand"],
        "country": req["country"],
        "location": {
            "lng": req["customer"]["lat"],
            "lat": req["customer"]["lon"]
        },
        "count": len([s for s in req["swimlanes"] if len(s["restaurant_ids"]) > 0]),
        "total": len(req["swimlanes"]),
        "platform": friendly_useragent,
        "original": req
    }
