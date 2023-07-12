import typing

from starlette.responses import Response, JSONResponse
from starlette.requests import Request

from common.base_endpoints import JwtEndpoint
from common.exceptions import AuthException, SessionExpireException
from ..extensions import jwt
from .. import models


class LoginEndpoint(JwtEndpoint):
    JWT_KEY = 'admin_token'
    jwt = jwt

    async def post(self, req: Request) -> JSONResponse:
        data = await req.json()
        user = await models.AdminUser.get(username=data['username'])
        if user.password != data['password']:
            raise AuthException("Wrong username or password")

        self.jwt_data = {'user_id': user.id}
        return JSONResponse({'name': user.username, 'avatar': ''})


class AuthRequireEndpoint(JwtEndpoint):
    JWT_KEY = LoginEndpoint.JWT_KEY
    jwt = jwt
    user: models.AdminUser

    async def on_request(self, req: Request):
        await super().on_request(req)
        if not self.jwt_data:
            raise SessionExpireException('Login required')

        self.user = await models.AdminUser.get(id=self.jwt_data["user_id"])
        assert self.user


class UserEndpoint(AuthRequireEndpoint):
    async def get(self, req: Request) -> JSONResponse:
        user_id = req.query_params.get('id')
        user = await models.AdminUser.get(id=user_id)
        return JSONResponse(user.to_dict())


class SingleChoiceEndpoint(AuthRequireEndpoint):
    async def get(self, req: Request) -> JSONResponse:
        pk = req.query_params.get('id')
        if pk:
            sc = await models.SingleChoice.get(id=pk)
            return JSONResponse(sc.to_dict())

        scs = await models.SingleChoice.all()
        return JSONResponse([sc.to_dict() for sc in scs])



