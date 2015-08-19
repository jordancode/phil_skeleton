from app.app import App
from framework.config.routes import Routes 

#creates a wsgi interface
app = App(Routes().get_map())