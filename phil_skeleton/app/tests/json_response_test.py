from werkzeug.test import Client
from run import app
from pprint import pprint

class JSONResponseTest:
    
    def run(self):

        c = Client(app)
        
        paths = [
                    '/user/me/',
                    '/user/54321/',
                    '/users/',
                    '/users',
                    '/broken/'
                ]
        for path in paths:
        
            print("attempting: " + path)
            
            app_iter, status, headers = c.get(path,base_url="http://api.photovault.com")
            
            pprint(status)
            pprint(headers)
            
            for line in app_iter:
                pprint(line)
            
            print("\n-------------\n")
        
        