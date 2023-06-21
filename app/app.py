import logging
import typing

from starlette.applications import Starlette
from starlette.routing import BaseRoute


class App(Starlette):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger(self.__class__.__name__)

    def register_routes(self, routes: typing.List[BaseRoute]):
        self.routes.extend(routes)
        for r in routes:
            self.logger.debug(f"Add route: {r}")
