from typing import ( Any, List )

def Module(
    imports: List[Any] = [],
    controllers: List[Any] = [],
    providers: List[Any] = [],
    exports: List[Any] = []
):
    def decorator(ClassBasedView):
        class IModule(ClassBasedView):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.imports=imports
                self.controllers=controllers
                self.providers=providers
                self.exports=exports
                
        return IModule
    return decorator