from user_agents import parse
def transform(req):
    useragent = parse(req["user_agent"])
    return {
        "brand": req['brand'],
        "location": {
            "lat": req["customer"]["lat"],
            "lng": req["customer"]["lon"]
        },
        "count": len(req["swimlanes"]),
        "platform": useragent.os if useragent.is_mobile else useragent.browser
    }