from dataclasses import dataclass

@dataclass
class User:
    username: str
    age: int
    active: bool = True

u = User("alice", 25)
print(u)