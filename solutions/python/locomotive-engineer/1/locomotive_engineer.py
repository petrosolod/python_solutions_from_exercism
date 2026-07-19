"""Functions which helps the locomotive engineer to keep track of the train."""
#from orca.sound import args


def get_list_of_wagons(*args):
    """Return a list of wagons, given an arbitrary amount of wagon numbers.

    Parameters:
        An arbitrary number of wagon numbers, unpacked.

    Returns:
        list: A list of wagon numbers.
    """
    return [*args]


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    Parameters:
        each_wagons_id (list[int]): The list of wagons.
        missing_wagons (list[int]): The list of missing wagons.

    Returns:
        list[int]: The corrected list of wagons.
    """
    second, fifth, first_id, *rest = each_wagons_id
    missing = missing_wagons


    return [first_id, *missing, *rest, second, fifth]


def add_missing_stops(route, **kwargs):
    missed_stops = list(kwargs.values())

    full_route = route.copy()
    full_route.update(stops=missed_stops)

    return full_route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    Parameters:
        route (dict): The route information.
        more_route_information (dict): The extra route information.

    Returns:
        dict: The extended route information.
    """
    extended_route = route|more_route_information
    return extended_route


def fix_wagon_depot(wagons_rows):
    """
    Fix the list of rows of wagons.

    Parameters:
        wagons_rows (list[list[tuple]]): The list of rows of wagons.

    Returns:
        list[list[tuple]]: the list of rows of wagons.
    """
    fixed_rows = []
    unpacked_rows = zip(*wagons_rows)

    for row in unpacked_rows:
        fixed_rows.append(list(row))

    return fixed_rows
