class ValidatedAge:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not (0 <= value <= 120):
            raise ValueError(f"{self.name} must be between 0 and 120")
        instance.__dict__[self.name] = value

class User:
    age = ValidatedAge()

u = User()
u.age = 25  
