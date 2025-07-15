def swap_case(s):
    swapCase = ""
    for char in s:
        if char.islower(): swapCase += char.upper()
        elif char.isupper(): swapCase += char.lower()
        else: swapCase += char
    return swapCase

