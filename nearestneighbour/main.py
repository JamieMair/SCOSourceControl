import numpy as np

""" 

"""
def generate_point_cloud(n:int, d:int = 2, seed=1234) -> np.ndarray:
    """Generates an array of d dimensional points in the range of [0, 1). The function generates n points. The result is stored in a n x d numpy array. 

    Args:
        n (int): The number of discrete points to generate.
        d (int, optional): The dimensionality of each point. Defaults to 2.
        seed (int, optional): The random seed used to generate the array. Defaults to 1234.

    Returns:
        np.ndarray: An n x d array of random numbers, whose coordinates are uniformly generated between [0, 1).
    """
    initial_seed = np.random.get_state()
    np.random.seed(seed)
    points = np.random.rand(n, d)
    np.random.set_state(initial_seed)
    return points


def find_nearest_neighbour_from_point(point_cloud:np.ndarray, point:int) -> int:
    """Finds the index of the point which is nearest to a given point, specified by an index

    Args:
        point_cloud (np.ndarray): The point cloud data stored in a n x d array, where n is the number of points and d is the dimensionality of each point.
        point (int): The index of the point in the point cloud.

    Returns:
        int: The index of the nearest point
    """
    pass