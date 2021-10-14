import numpy as np
import matplotlib.pyplot as plt


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
    """Finds the index of the point in a given point cloud which is nearest to an input point, specified by an index

    Args:
        point_cloud (np.ndarray): The point cloud data stored in a n x d array, where n is the number of points and d is the dimensionality of each point.
        point (int): The index of the point in the point cloud.

    Returns:
        int: The index of the nearest point
    """
    pass


def find_all_nearest_neighbours(point_cloud:np.ndarray) -> np.ndarray:
    """Finds the nearest neighbour of each point in the point cloud and returns the index of that point in a list.


    Args:
        point_cloud (np.ndarray): The point cloud data stored in a n x d array, where n is the number of points and d is the dimensionality of each point.

    Returns:
        np.ndarray: An n dimensional array array of integers. Each element corresponds to a point in the point cloud, and the value contained is the index
        of the nearest point in the point_cloud array.
    """
    pass


def plot_point_cloud(point_cloud:np.ndarray):
    """Plots a graph showing the point cloud. The point cloud must have a dimensionality less than or equal to 3.

    Args:
        point_cloud (np.ndarray): The point cloud data stored in a n x d array, where n is the number of points and d is the dimensionality of each point. d must be less than 4.
    """

    n, d = np.shape(point_cloud)
    assert d <= 3, "In order to plot, the points must be less than 4D."

    fig = plt.figure()
    if d == 1:
        __plot_point_cloud_1D(point_cloud)
    elif d==2:
        __plot_point_cloud_2D(point_cloud)
    elif d==3:
        __plot_point_cloud_3D(point_cloud)
    else:
        raise Exception("Unrecognised dimensionality for plotting.")
    return fig


def __plot_point_cloud_1D(point_cloud:np.ndarray):
    """Plots a graph showing a 1 dimensional point cloud.

    Args:
        point_cloud (np.ndarray): The point cloud data stored in a n x 1 array, where n is the number of points.
    """
    pass


def __plot_point_cloud_2D(point_cloud:np.ndarray):
    """Plots a graph showing a 2 dimensional point cloud.

    Args:
        point_cloud (np.ndarray): The point cloud data stored in a n x 2 array, where n is the number of points.
    """
    pass


def __plot_point_cloud_3D(point_cloud:np.ndarray):
    """Plots a graph showing a 3 dimensional point cloud.

    Args:
        point_cloud (np.ndarray): The point cloud data stored in a n x 3 array, where n is the number of points.
    """
    pass

def plot_2D_nearest_neighbours(point_cloud:np.array, nearest_neighbours:np.ndarray=None):
    """Plots a 2D scatter graph of a point cloud, withs arrows from each point to their nearest neighbour.

    Args:
        point_cloud (np.array): The point cloud data stored in a n x 2 array, where n is the number of points.
        nearest_neighbours (np.array, optional): An n dimensional array array of integers. Each element corresponds to a point in the point cloud, and the value contained is the index
        of the nearest point in the point_cloud array. Defaults to None.
    """
    n, d = np.shape(point_cloud)
    assert d==2, "Can only plot nearest neighbours for a 2D point cloud."
    # If the nearest neighbours are not already found, re-calculate.
    if nearest_neighbours is None:
        nearest_neighbours = find_all_nearest_neighbours(point_cloud)
    
    # TODO: Implement plotting here