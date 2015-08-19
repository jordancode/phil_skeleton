from app.tests.json_response_test import JSONResponseTest
from app.tests.template_response_test import TemplateResponseTest
from app.tests.mysql_test import MySQLTest
from app.tests.memcached_test import MemcachedTest
from app.tests.auth_test import AuthTest

#JSONResponseTest().run()
#TemplateResponseTest().run()
#MySQLTest.run()
#MemcachedTest.run()
AuthTest.run()