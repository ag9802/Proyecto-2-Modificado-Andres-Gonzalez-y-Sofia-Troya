def main():
    a = input("> ")
    b = encriptar(a)
    

def encriptar(a):
    guia = {
        "1" :"a",
        "2": "b",
        "3":"c",
        "4":"d",
        "5":"e",
        "6":"f",
        "7":"g",
        "8":"h",
        "9":"i",
        "0":"j",
        "<":"k",
        ">":"l",
        "'":"m",
        ",":"n",
        "#":"ñ",
        "$":"o",
        "%":"p",
        "&":"q",
        "/":"r",
        ")":"s",
        "(":"t",
        "[":"u",
        "]":"v",
        "{":"w",
        "}":"x",
        "-":"y",
        "_":"z",
        "a": "1",
        "b": "2",
        "c": "3",
        "d": "4",
        "e": "5",
        "f": "6",
        "g": "7",
        "h": "8",
        "i": "9",
        "j": "0",
        "k": "<",
        "l": ">",
        "m": "'",
        "n": ",",
        "ñ": "#",
        "o": "$",
        "p": "%",
        "q": "&",
        "r": "/",
        "s": ")",
        "t": "(",
        "u": "[",
        "v": "]",
        "w": "{",
        "x": "}",
        "y": "-",
        "z": "_",
    }
    outcome = " "
    for i in a:
        outcome += guia.get(i, i) 
    print(outcome)
    return outcome

if __name__ == "__main__":
    main()
