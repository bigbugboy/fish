import typing

from starlette.responses import Response, JSONResponse
from starlette.requests import Request

from common.base_endpoints import JwtEndpoint
from common.exceptions import AuthException, SessionExpireException
from ..extensions import jwt
from ..models import AdminUser, SingleChoice


class Login(JwtEndpoint):
    JWT_KEY = 'admin_token'
    jwt = jwt

    async def post(self, req: Request) -> JSONResponse:
        data = await req.json()
        if not (data['username'] == 'jwt' and data['password'] == 'bbb'):
            raise AuthException("Wrong username or password")

        self.jwt_data = {'user_id': 520}
        return JSONResponse({'name': 'jwt', 'avatar': ''})


class LoginRequireEndpoint(JwtEndpoint):
    JWT_KEY = Login.JWT_KEY
    jwt = jwt
    user: AdminUser

    # async def on_request(self, req: Request):
    #     await super().on_request(req)
    #     if not self.jwt_data:
    #         raise SessionExpireException('Login required')
    #
    #     self.user = await AdminUser.get(id=self.jwt_data["user_id"])
    #     assert self.user


class UserEndpoint(LoginRequireEndpoint):
    async def post(self, req: Request) -> JSONResponse:
        data = await req.json()
        print(111)
        print(data)
        return JSONResponse({})


class SingleChoiceEndpoint(LoginRequireEndpoint):
    async def get(self, req: Request) -> JSONResponse:
        pk = req.query_params.get('id')
        if pk:
            sc = await SingleChoice.get(id=pk)
            return JSONResponse(sc.to_dict())

        scs = await SingleChoice.all()
        return JSONResponse([sc.to_dict() for sc in scs])


