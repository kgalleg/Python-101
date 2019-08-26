def bake_a_cake(batter, temperature, time):
    oven = {
        "type": "electric",
        "model": "GE",
        "volume": 17,
        "contents": None,         #none is null - no value
        "temperature": 0
    }

    oven["contents"] = batter
    oven ["temperature"] = temperature

#using the parameters time and temperature
    return f'Your beautiful cake was baked for {time} at {temperature} degrees'