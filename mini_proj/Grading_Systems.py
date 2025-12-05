scores = int(input("Enter your score(0 - 100) "))

match scores:
    case _ if 90 <= scores <= 100:
        print("A")
    case _ if 80 <= scores <= 89:
        print("B")
    case _ if 70 <= scores <= 79:
        print("C")
    case _ if 60 <= scores <= 69:
        print("D")
    case _ if 0 <= scores <= 59:
        print("F")
    case _:
        print("Invalid Score")
