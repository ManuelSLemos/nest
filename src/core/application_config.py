from src.common.metadata import GlobalPrefixOptions, VersioningOptions

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class ApplicationConfig(metaclass=SingletonMeta):
    def __init__(self):
        self.globalPrefix: GlobalPrefixOptions
        self.versioning: VersioningOptions

