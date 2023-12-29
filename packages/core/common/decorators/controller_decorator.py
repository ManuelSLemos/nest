from fastapi import APIRouter

from typing import ( Any, List )


# TODO: Consider whether to implement host param
class Controller:
    def __init__(
        self, 
        prefix: str | List[str] = '/',
    ):
        self.prefix = prefix

    def __call__(decorator, ClassBasedView):
        class IController(ClassBasedView):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.prefix = decorator.prefix
                self.router = APIRouter(prefix=self.prefix)
                
                cls = ClassBasedView

                for attr_name in dir(cls):
                    attr = getattr(cls, attr_name)
                    if callable(attr) and hasattr(attr, "is_route"):
                        prefix, method = getattr(attr, "route_info")
                        print(prefix, method)
                        self.router.add_api_route(prefix, attr, methods=[method])


            def _module_attributes(classProperty: Any, attrName: str, decoratorProperty: Any):
                return classProperty if hasattr(decorator, attrName) else decoratorProperty
        
        IController.decorator = decorator
        return IController