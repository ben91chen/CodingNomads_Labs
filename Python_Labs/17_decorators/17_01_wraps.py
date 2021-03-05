'''
Write a decorator function that wraps text passed to it in a html <p> tag.

'''

def p_tag_wrapper(f):
    def decorator(text):
        text = f"<p>{f(text)}</p>"
        return text
    return decorator

@p_tag_wrapper
def sentence(text):
    return text

print(sentence("hello"))

