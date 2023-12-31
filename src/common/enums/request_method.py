from enum import Enum

class RequestMethod(Enum):
    GET = 0,
    POST = 1,
    PUT = 2,
    DELETE = 3,
    PATCH = 4,
    OPTIONS = 5,
    HEAD = 6,
    SEARCH = 7,
    ALL = 8,
