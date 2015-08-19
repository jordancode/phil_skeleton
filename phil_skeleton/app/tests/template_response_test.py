from werkzeug.test import Client
from run import app
from pprint import pprint

class TemplateResponseTest:
    
    def run(self):

        c = Client(app)
        
        
        app_iter, status, headers = c.get('/',base_url="http://www.photovault.com")
        
        pprint(status)
        pprint(headers)
        
        for line in app_iter:
            pprint(line)
        
        
        