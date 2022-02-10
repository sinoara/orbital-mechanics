"""
Physics functions
"""
import numpy as np


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
    return np.double(0.0)
