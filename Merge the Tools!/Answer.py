import textwrap

def merge_the_tools(string, k):
    wrapper = textwrap.TextWrapper(width = k)
    word_list = wrapper.wrap(text = string)
    for i in word_list:
        result = ""
        for j in i:
            if j not in result:
                result += j
        print(result)
