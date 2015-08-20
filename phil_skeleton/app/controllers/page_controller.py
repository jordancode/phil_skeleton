from framework.controllers.base_controller import BaseController
from framework.http.partial_page_response import PartialPageResponse
from framework.http.page_response import PageResponse

class PageController(BaseController):

    def index(self):
        
        data = {
            "message" : "Hello World!"
         }
        
        
        return PageResponse("index_content", data)
        
