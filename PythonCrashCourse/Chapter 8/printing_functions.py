# 8-15
import print_models as pm


pm.print_models(unprinted_designs='', completed_models='')
pm.show_completed_models(completed_models='')

# 8-16
import pizza_function
pizza_function.make_pizza(16, 'pepperoni')

from pizza_function import make_pizza
make_pizza(15, 'peppers')

from pizza_function import make_pizza as mp
mp(14,'sausage')

import pizza_function as fn
fn.make_pizza(13, 'devil lettuce')

from pizza_function import *

make_pizza(12, 'onions')





