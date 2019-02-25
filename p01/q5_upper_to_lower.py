ch = input("Enter a uppercase alphabet: ")
if ch.isupper() and len(ch) == 1:
    print("Lowercase character: " + ch.lower())
else:
    print("Eh? Not uppercase character!")
