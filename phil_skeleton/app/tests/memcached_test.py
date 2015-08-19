from pprint import pprint
from framework.storage.cache import Cache

class MemcachedTest:
    
    @staticmethod
    def run():
        
        mc = Cache.get_instance()
        
        mc.set("test","hi")
        pprint(mc.get("test"))