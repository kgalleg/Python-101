
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


def make_better_cake_batter(ingredients):
    cake_batter_mass = 0
    for value in ingredients.values():
        cake_batter_mass += value

    return cake_batter_mass

def get_ingredients():

#diccionary (object in js)
    ingredients = {
        "flour": 10,
        "sugar": 3,
        "eggs": 6,
        "butter": 2,
        "baking_powder": 1,
        "vanilla": 0.5
    }

    return ingredients

#modules need to be very concise and do only one job only.
#one module to bake the cake, another to get the ingredients, one module to batter.


# only need import
# don't need to export anymore

