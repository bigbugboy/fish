from tortoise.contrib.starlette import register_tortoise

from app.app import App
from app.routes import ROUTES


app = App()
app.debug = True
app.register_routes(ROUTES)

register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",   # todo: use mysql
    modules={"models": ["app.models"]},
    generate_schemas=True
)
