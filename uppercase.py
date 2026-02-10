
class ForceUppercase(type):
    def __new__(cls, name, bases, dct):
        uppercase_attrs = {k.upper(): v for k, v in dct.items() if not k.startswith("__")}
        return super().__new__(cls, name, bases, uppercase_attrs)

class MyAPI(metaclass=ForceUppercase):
    endpoint = "/login"
    timeout = 30
print(MyAPI.ENDPOINT) 
