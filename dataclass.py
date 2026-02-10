from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0

    def total_value(self) -> float:
        return self.price * self.quantity

# No need to write an __init__ method!
item = Product("Mechanical Keyboard", 120.50, 2)

print(item)  # Automatically generates a clean string representation
# Output: Product(name='Mechanical Keyboard', price=120.5, quantity=2)