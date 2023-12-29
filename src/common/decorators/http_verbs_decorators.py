def Delete(prefix: str = '/'):
    return _http_verb(prefix, 'DELETE')

def Get(prefix: str = '/'):
    return _http_verb(prefix, 'GET')

def Head(prefix: str = '/'):
    return _http_verb(prefix, 'HEAD')

def Options(prefix: str = '/'):
    return _http_verb(prefix, 'OPTIONS')

def Path(prefix: str = '/'):
    return _http_verb(prefix, 'PATH')

def Post(prefix: str = '/'):
    return _http_verb(prefix, 'POST')

def Put(prefix: str = '/'):
    return _http_verb(prefix, 'PUT')

def _http_verb(prefix: str, method: str):
    def decorator(fn):
        setattr(fn, "is_route", True)
        setattr(fn, "route_info", (prefix, method))
        return fn
    return decorator