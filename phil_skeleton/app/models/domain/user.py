from framework.models.domain.entity import Entity

class User(Entity):
    
    def __init__(self, id, full_name, email):
        super().__init__(id)
        
        self._set_inital_attr("full_name",full_name)
        self._set_inital_attr("email",email)
    
    
    def get_first_name(self):
        return self.get_full_name().split(1)[0]
    
    def get_full_name(self):
        return self._get_attr("full_name")
    
    def get_email(self):
        return self._get_attr("email")