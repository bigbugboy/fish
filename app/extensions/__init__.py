import typing

import settings
from common.extensions.jwtext import Jwt
from common.app import ExtensionMixin


jwt = Jwt(**settings.JWT)


EXTENSIONS: typing.List[ExtensionMixin] = [
    jwt,
]
