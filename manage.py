from app.app import App
from app.routes import ROUTES


app = App()
app.debug = True
app.register_routes(ROUTES)

