import typing

from starlette.routing import BaseRoute, Route

from .endpoints import Hello


ROUTES: typing.List[BaseRoute] = [
    Route("/hello", Hello),
]
