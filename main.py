from speech import listen
from parser import parse

def main():
    print("CAIDET is live. Speak your command...")

    command = listen()
    print("Heard:", command)

    parsed = parse(command)
    print("Parsed command:", parsed)

if __name__ == "__main__":
    main()

