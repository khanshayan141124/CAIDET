def listen():
    """
    Simulates voice input.
    Later this will be replaced by real speech-to-text.
    """
    command = input("🎙️ You: ")
    return command.lower()
