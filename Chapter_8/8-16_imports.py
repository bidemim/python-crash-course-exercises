# importing sandwiches using different methods
import sandwiches
sandwiches.sandwich_fillings('cabbage', 'mayo')

from sandwiches import sandwich_fillings
sandwich_fillings('cabbages', 'tomatoes', 'peanut butter')

from sandwiches import sandwich_fillings as sf
sf('strawberry jam', 'peanut butter', 'sesame seed', 'butter')

import sandwiches as sw
sw.sandwich_fillings('tomato', 'mustard', 'cabbages')

from sandwiches import *
sandwich_fillings('mustard', 'cheese', 'eggs')


