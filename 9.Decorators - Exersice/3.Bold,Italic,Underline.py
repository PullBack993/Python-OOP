def make_bold(func):
    def wrapper(*names):
        return f"<b>{func(*names)}</b>"
    return wrapper

def make_italic(func):
    def wrapper(*names):
        return f"<i>{func(*names)}</i>"
    return wrapper

def make_underline(func):
    def wrapper(*names):
        return f"<u>{func(*names)}</u>"
    return wrapper


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))

