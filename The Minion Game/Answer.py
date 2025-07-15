def minion_game(string):
    stuart = 0
    kevin = 0
    for i in range(len(string)):
        if string[i] in "AEIOU":
            kevin += (len(string) - i)
        else:
            stuart += (len(string) - i)
    if stuart > kevin: print(f"Stuart {stuart}")
    elif stuart < kevin: print(f"Kevin {kevin}")
    else : print("Draw")
