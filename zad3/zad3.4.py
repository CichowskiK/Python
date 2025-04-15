while True:
    user_input = input("Podaj liczbe lub wpisz \"stop\" aby zakonczyc\n")
    
    if user_input.lower() == 'stop':
        break
    
    try:
        x = float(user_input)
        print("Liczba: ",x , "\ndo trzeciej potegi ",x ** 3)
    except ValueError:
        print("invalid input")