from pprint import pprint
from framework.models.domain.authentication import Authentication, AuthException
from framework.models.services.auth_service import AuthService
from framework.models.data_access.base_user_dao import BaseUserDAO

class AuthTest:
    
    @staticmethod
    def run():
        
        auth_service = AuthService()
        
        user1 = BaseUserDAO().new_user()
        
        try:
            res = auth_service.add_auth_to_user(user1, Authentication, "user1", "secret_password", "test_ua" )
            
            assert res
            
        except AuthException as ae:
            print("Test 1 failed: " + str(ae))
        
        
        try:
            res = auth_service.add_auth_to_user(user1, Authentication, "user1", "secret_password4", "test_ua" )
            
            assert not res
            
        except AuthException as ae:
            print("Test 2 Success: " + str(ae))
        
        
        user2 = BaseUserDAO().new_user()
        
        
        try:
            res = auth_service.add_auth_to_user(user2, Authentication, "user2", "secret_password", "test_ua" )
            
            assert res
            
        except AuthException as ae:
            print("Test 3 failed: " + str(ae))
        
        
        
        try:
            session = auth_service.log_in(Authentication, "user1", "secret_password2", "test_ua")
            assert not session
            
            pprint( session)
            
        except AuthException as ae:
            print("Test 4 success: " + str(ae))
        
        
        try:
            session = auth_service.log_in(Authentication, "user1", "secret_password", "test_ua")
            assert session.user.id
            
            pprint(session.user)
            
        except AuthException as ae:
            print("Test 5 failed: " + str(ae))
        