import typing

from starlette.routing import BaseRoute, Route

from app.endpoints import admin
from app.endpoints.web import Hello, SingleChoiceEndpoint


ROUTES: typing.List[BaseRoute] = [
    Route("/hello", Hello),
    Route("/single_choice", SingleChoiceEndpoint),
    # admin api list
    Route('/api/admin/login', admin.Login),
    Route('/api/admin/user', admin.AdminUser),
    Route('/api/admin/sc', admin.SingleChoiceEndpoint),
]
