def translator(i):
    if i == "a":
        return "*-"
    elif i == "b":
        return "-***"  
    elif i == "c":
        return "-*-*" 
    elif i == "d":
        return "-**"
    elif i == "e":
        return "*"
    elif i == "f":
        return "**-*"
    elif i == "g":
        return "--*"
    elif i == "h":
        return "****"
    elif i == "i":
        return "**"
    elif i == "j":
        return "*---"
    elif i == "k":
        return "-*-"
    elif i == "l":
        return "*-**"
    elif i == "m":
        return "--"
    elif i == "n":
        return "-*"
    elif i == "o":
        return "---"
    elif i == "p":
        return "*--*"
    elif i == "q":
        return "--*-"
    elif i == "r":
        return "*-*"
    elif i == "s":
        return "***"
    elif i == "t":
        return "-"
    elif i == "u":
        return "**-"
    elif i == "v":
        return "***-"
    elif i == "w":
        return "*--"
    elif i == "x":
        return "-**-"
    elif i == "y":
        return "-*--"
    elif i == "z":
        return "--**"
    elif i == "1":
        return "*----"
    elif i == "2":
        return "**---"
    elif i == "3":
        return "***--"
    elif i == "4":
        return "****-"
    elif i == "5":
        return "*****"
    elif i == "6":
        return "-****"
    elif i == "7":
        return "--***"
    elif i == "8":
        return "---**"
    elif i == "9":
        return "----*"
    elif i == "0":
        return "-----"                 

print("Dot is * and Dash is -")
print("")

t = ["l"]
for num in t:
    try:
        s = str(input("Enter word here: ")).lower()
        print("")
    except:
        print("Error. That is not word.")
        t.append("l")
        continue

def iterator(w):
    i = 0
    l = []
    result = ""
    while i <= len(w) - 1:
        l.append(translator(w[i]))
        i += 1

    return result.join(l)

print(iterator(s))        
            