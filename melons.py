class Watermelon (object):
    color = "green"
    is_imported = False
    shape = "natural" 
    seasons = ["fall", "summer"]
    price = 5.00

class Cantaloupe (object):
    color = "tan"
    is_imported = False
    shape = "natural"
    seasons = ["spring", "summer"]
    price = 5.00

class Casaba (object):
    color = "green"
    is_imported = True
    shape = "natural"
    seasons = ["spring", "summer", "fall", "winter"]
    price = 9.00

class Sharlyn (object):
    color = "tan"
    is_imported = True
    shape = "natural"
    seasons = ["summer"]
    price = 7.50

class SantaClaus (object):
    color = "green"
    is_imported = True
    shape = "natural"
    seasons = ["winter", "spring"]
    price = 7.50

class Christmas (object):
    color = "green"
    is_imported = False
    shape = "natural"
    seasons = ["winter"]
    price = 5.00

class HornedMelon (object):
    color = "yellow"
    is_imported = True
    shape = "natural"
    seasons = ["summer"]
    price = 7.50

class Xigua (object):
    color = "black"
    is_imported = True
    shape = "square"
    seasons = ["summer"]
    price = 10.50

class Ogen (object): 
    color = "tan"
    is_imported = False
    shape = "natural"
    seasons = ["spring", "summer"]
    price = 6.00



def get_price(qty):
    """Determine price for this quantity of melons of this type.

    Return a float of the total price.
    """

