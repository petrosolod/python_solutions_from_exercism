EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(min_in_oven):
    """some notes"""
    return EXPECTED_BAKE_TIME - min_in_oven

def preparation_time_in_minutes(number_of_layers):
    """some notes"""
    return PREPARATION_TIME * number_of_layers
    
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):

    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

    