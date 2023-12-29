from typing import ( Any, List )

# TODO: Consider whether to implement host param
class Controller:
    def __init__(
        self, 
        path: str | List[str] = '/',
        # host: str
    ):
        self.path = path
        # self.host = host

    def __call__(decorator, ClassBasedView):
        class IController(ClassBasedView):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.path = decorator.path
                # self.host = decorator.host

            def _module_attributes(classProperty: Any, attrName: str, decoratorProperty: Any):
                return classProperty if hasattr(decorator, attrName) else decoratorProperty
        
        IController.decorator = decorator
        return IController