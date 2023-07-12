from starlette.endpoints import HTTPEndpoint

from ..tools.jwttools import JWT


class JwtEndpoint(HTTPEndpoint):

    jwt: JWT
    