from tortoise.contrib.starlette import register_tortoise

from app.app import App
from app.routes import ROUTES
from app.middlewares import MIDDLEWARES
import settings


app = App()
app.debug = True
app.register_routes(ROUTES)
app.register_middlewares(MIDDLEWARES)

register_tortoise(
    app,
    db_url=settings.MYSQL['url'],
    modules={'models': ['app.models']},
    generate_schemas=True
)
