from starlette.endpoints import HTTPEndpoint
from starlette.responses import Response


class Hello(HTTPEndpoint):
    async def get(self, _):
        return Response("hello")
