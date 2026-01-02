FILLER_WORDS = ["uh", "um", "uhm", "hmm", "hmmm", "like"]

def remove_fillers(text):
    words = text.split()
    clean_words = [w for w in words if w not in FILLER_WORDS]
    return " ".join(clean_words)


def parse(command):
    """
    Converts spoken command into structured intent
    """
    clean = remove_fillers(command)

    if "add" in clean and "for loop" in clean:
        return {
            "action": "add_loop",
            "type": "for"
        }

    if "add" in clean and "while loop" in clean:
        return {
            "action": "add_loop",
            "type": "while"
        }

    if "declare" in clean and "integer" in clean:
        return {
            "action": "declare_variable",
            "datatype": "int"
        }

    return {
        "action": "unknown",
        "raw": clean
    }
