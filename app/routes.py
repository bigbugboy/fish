import typing

from starlette.routing import BaseRoute, Route

from .endpoints import Hello, SingleChoiceEndpoint


ROUTES: typing.List[BaseRoute] = [
    Route("/hello", Hello),
    Route("/single_choice", SingleChoiceEndpoint)
]
