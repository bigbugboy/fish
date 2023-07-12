import typing

from starlette.routing import BaseRoute, Route

from app.endpoints import admin


ROUTES: typing.List[BaseRoute] = [
    Route('/api/admin/login', admin.LoginEndpoint),
    Route('/api/admin/user', admin.UserEndpoint),
    Route('/api/admin/sc', admin.SingleChoiceEndpoint),
]
