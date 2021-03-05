'''
Improve the decorator from the previous exercise by allowing it to take
any specified HTML tag as an input - making it more general.

'''

def tag_wrapper(tag):
    def html_tag(f):
        def decorator(text):
            text = f"<{tag}>{f(text)}</{tag}>"
            return text
        return decorator
    return html_tag

# @tag_wrapper('p')
# @tag_wrapper('b')
def sentence(text):
    return text

sentence = tag_wrapper('b')(sentence)
print(sentence("hello"))