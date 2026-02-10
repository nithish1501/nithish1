from contextlib import contextmanager

@contextmanager
def managed_resource(name):
    print(f"Connecting to resource: {name}")
    try:
        # This is where the "yield" hands control back to the 'with' block
        yield f"Data from {name}"
    finally:
        # This runs no matter what happens in the 'with' block
        print(f"Closing connection to {name}")

with managed_resource("Secure_Database") as data:
    print(f"Working with: {data}")