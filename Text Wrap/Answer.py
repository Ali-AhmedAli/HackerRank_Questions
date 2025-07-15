import textwrap
def wrap(string, max_width):
    result = ""
    wrapper = textwrap.TextWrapper(width=max_width)
    result = wrapper.fill(text=string)
    return result