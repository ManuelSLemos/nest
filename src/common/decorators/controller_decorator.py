from fastapi import APIRouter
from pydantic import BaseModel
from typing import ( Any, List, Optional )

class Route(BaseModel):
    prefix: str
    attr: Any
    method: str


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
                self.prefix = self.set_prefix(decorator.prefix)
                self.tags = self.set_tag(decorator.prefix)
                self.routes = self.set_routes()

            def set_routes(self) -> List[Any]:
                endpoints = []

                for attr_name in dir(ClassBasedView):
                    attr = getattr(ClassBasedView, attr_name)

                    if callable(attr) and hasattr(attr, 'is_route'):
                        prefix, method = getattr(attr, 'route_info')

                        endpoints.append(Route(
                            prefix=prefix,
                            attr=attr,
                            method=method                
                        ))

                return endpoints
            
            def set_prefix(self, value: str) -> str:
                if not value.startswith("/"):
                    value = f'/{value}'

                if value.endswith("/"):
                    value = value[:-1]

                return value
            
            # TODO: Create options kind tag in DocsOptions
            def set_tag(self, value: str) -> Optional[List[str]]:
                if value.__eq__('/'):
                    return ['/']
                
                return [ self.set_prefix(value) ]

            def _module_attributes(classProperty: Any, attrName: str, decoratorProperty: Any):
                return classProperty if hasattr(decorator, attrName) else decoratorProperty
        
        IController.decorator = decorator
        return IController