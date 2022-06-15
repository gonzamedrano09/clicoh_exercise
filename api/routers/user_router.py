from rest_framework.routers import Route, DynamicRoute, SimpleRouter


class UserRouter(SimpleRouter):
    routes = [
        Route(
            url=r"^{prefix}{trailing_slash}$",
            mapping={"post": "create",
                     "get": "retrieve",
                     "delete": "destroy"},
            name="{basename}-list",
            detail=False,
            initkwargs={"suffix": "List"}
        ),
        DynamicRoute(
            url=r"^{prefix}/{url_path}{trailing_slash}$",
            name="{basename}-{url_name}",
            detail=False,
            initkwargs={}
        )
    ]
