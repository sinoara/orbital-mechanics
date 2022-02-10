"""
Physics functions
"""
import numpy as np

from scipy.constants import G # type: ignore[import]

from .geometry import distance
from .body import Body


def gravity_force(body1: Body, body2: Body) -> np.double:
    """Calculates gravity force between two bodies

    Parameters
    ----------
    body1 : Body
        First body.
    body2 : Body
        Second body.

    Returns
    -------
    force : float
        Force between `body1` and `body2`..
    """
    dist = distance(body1, body2)
    mass1 = body1.mass
    mass2 = body2.mass
    return G*mass1*mass2/dist**2
