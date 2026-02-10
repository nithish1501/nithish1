def handle_command(command):
    match command.split():
        case ["quit"]:
            print("Shutting down...")
        case ["load", filename]:
            print(f"Loading {filename}")
        case ["move", x, y] if int(y) > 0:
            print(f"Moving to {x}, {y} (Northward)")
        case _:
            print("Unknown command")

handle_command("move 10 20")