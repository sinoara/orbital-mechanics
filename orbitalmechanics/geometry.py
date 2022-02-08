"""
Geometry functions
"""

import numpy as np

from .body import Body


def distance(body1: Body, body2: Body) -> np.double:
    """Calculates distance between two bodies

    Parameters
    ----------
    body1 : Body
        First body.
    body2 : Body
        Second body.

    Returns
    -------
    distance : float
        Distance between `body1` and `body2`..
    """
    pos1 = body1.current_position
    pos2 = body2.current_position
    dist = np.sqrt(np.square(pos1-pos2).sum())
    return dist
