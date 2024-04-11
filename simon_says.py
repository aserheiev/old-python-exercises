instructions = input()

def what_to_do(instructions):
    if instructions.endswith("Simon says"):
        instructions = "I " + instructions.replace("Simon says", "")
        return instructions
    elif instructions.startswith("Simon says"):
        instructions = "I " + instructions.replace("Simon says", "")
        return instructions
    else:
        return "I won't do it!"

print(what_to_do(instructions))


def what_to_do(instructions):
    if instructions.endswith("Simon says"):
        return "I " + instructions[:len("Simon says") + 1]
    elif instructions.startswith("Simon says"):
        return "I" + instructions[len("Simon says"):]
        
    return "I won't do it!"