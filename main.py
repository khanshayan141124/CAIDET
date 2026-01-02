from speech import listen
from parser import parse

# Define what each action does
def handle_command(parsed):
    action = parsed.get("action")
    cmd_type = parsed.get("type")

    if action == "add_loop":
        if cmd_type == "for":
            print("for i in range(10):")
            print("    pass")
        elif cmd_type == "while":
            print("while True:")
            print("    pass")

    elif action == "add_print":
        message = parsed.get("message", "Hello, World!")
        print(f'print("{message}")')

    elif action == "add_variable":
        var_name = parsed.get("name", "x")
        var_value = parsed.get("value", "0")
        print(f"{var_name} = {var_value}")

    else:
        print("Action not recognized!")

def main():
    print("CAIDET is live. Speak your command...")

    command = listen()
    print("Heard:", command)

    parsed = parse(command)
    print("Parsed command:", parsed)

    handle_command(parsed)

if __name__ == "__main__":
    main()

