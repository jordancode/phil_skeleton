from framework.base_application import BaseApplication
from framework.config.config import Config


class App(BaseApplication):
    
    def get_server_name(self):
        return Config.get("app","server_name")
    
    def pre_hook(self,request):
        pass
    
    def post_hook(self,request,response):
        pass