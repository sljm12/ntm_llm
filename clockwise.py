def find_center(points):
    """Finds the center of a list of (x,y) points.

    Args:
    points: A list of (x,y) tuples.

    Returns:
    A tuple representing the center point (x,y).
    """

    x_coords = [x for x, _ in points]
    y_coords = [y for _, y in points]

    center_x = sum(x_coords) / len(x_coords)
    center_y = sum(y_coords) / len(y_coords)

    return center_x, center_y

    # Example usage:
    points = [(1, 2), (3, 4), (5, 6), (7, 8)]
    center = find_center(points)
    print(center)  # Output: (4.0, 5.0)

from math import atan2

def argsort(seq):
    #http://stackoverflow.com/questions/3382352/equivalent-of-numpy-argsort-in-basic-python/3382369#3382369
    #by unutbu
    #https://stackoverflow.com/questions/3382352/equivalent-of-numpy-argsort-in-basic-python 
    # from Boris Gorelik
    return sorted(range(len(seq)), key=seq.__getitem__)

def rotational_sort(list_of_xy_coords, centre_of_rotation_xy_coord, clockwise=True):
    cx,cy=centre_of_rotation_xy_coord
    angles = [atan2(x-cx, y-cy) for x,y in list_of_xy_coords]
    indices = argsort(angles)
    if clockwise:
        return [list_of_xy_coords[i] for i in indices]
    else:
        return [list_of_xy_coords[i] for i in indices[::-1]]
    
point = [99.5, 5.5], [99.5, 5.0], [100.0, 6.0], [100.0, 5.5]

centre = find_center(point)
print(centre)

print(rotational_sort(point, centre))

from geographiclib.geodesic import Geodesic

def sort_points_clockwise(points):
    """Sorts a list of WGS-84 coordinates in clockwise order.

    Args:
        points: A list of tuples (lat, lon).

    Returns:
        A list of sorted points.
    """

    geod = Geodesic.WGS84  # Use WGS84 ellipsoid

    def get_azimuth(p1, p2):
        g = geod.Inverse(p1[0], p1[1], p2[0], p2[1])
        return g['azi1']

    # Find the point with the smallest latitude
    min_lat_point = min(points, key=lambda p: p[0])

    # Sort points based on azimuth from the min_lat_point
    sorted_points = sorted(points, key=lambda p: get_azimuth(min_lat_point, p))

    return sorted_points

print(sort_points_clockwise(point))
