def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b
    else:
        return "Unknown operation"


def word_counter(text):
    words = text.split()
    return len(words)


def text_uppercase(text):
    return text.upper()
