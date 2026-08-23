from collections import namedtuple
from enum import Enum, unique

size = namedtuple("size", ["x", "y"])


@unique
class paper_size(Enum):
    """Standard (ISO216) paper sizes in mm"""

    A0 = size(x=841, y=1189)
    A1 = size(x=594, y=841)
    A2 = size(x=420, y=594)
    A3 = size(x=297, y=420)
    A4 = size(x=210, y=297)
    A5 = size(x=148, y=210)
    A6 = size(x=105, y=148)
    A7 = size(x=74, y=105)
    A8 = size(x=52, y=74)
    A9 = size(x=37, y=52)
    A10 = size(x=26, y=37)
