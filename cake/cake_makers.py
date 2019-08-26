# only need import
# don't need to export anymore

from bake import bake_a_cake
from batter import make_better_cake_batter
from ingredietns import get_ingredients

ingredients = get_ingredients()
batter = make_better_cake_batter(ingredients)
cake_result = bake_a_cake(batter, 350, 45)

print(cake_result)





