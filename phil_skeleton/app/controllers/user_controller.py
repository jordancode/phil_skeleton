from framework.base_controller import BaseController
from framework.http.json_response import JSONResponse

class UserController(BaseController):

	def get_me(self):
		return self.get(123)
	
	def get(self,user_id):
		user = {
				"name" : "Bob Dobalina",
				"id" : user_id
			}
		
		return JSONResponse(user)
		
	
	def create(self):
		JSONResponse({"id":1234})
