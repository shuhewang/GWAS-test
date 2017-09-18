def main(): #This is a game called Lunar Lander.
    print("Welcome to Lunar Lander")
    a = 1000.0
    b = 0.0
    c = 1000.0
    altitude = a
    velocity = b
    fuel = c
    user_input = answer()
    while user_input == 'y':
        a = 1000.0
        b = 0.0
        c = 1000.0
        print("altitude=", a, "meters,", "velocity=", b, "meters/second,", "fuel=", c, "liters")
        while a > 0:
            e = float(input("How much fuel do you want to burn?"))
            if e >= c:
                e = c
            else:
                e = e
            b = b + 1.6 - 0.15 * e
            a = a - b
            c = c - e
            print("altitude=", a, "meters,", "velocity=", b, "meters/second,", "fuel=", c, "liters")
        if b <= 10:
            print("Bravo! Land safely!")
        else:
            print("Blast! Oooooooz")
        user_input = answer()

def answer():
    user_input = input("Do you want to continue the game? Enter \"y\" for yes or \"n\" for no ")
    if user_input == 'y':
        return 'y'        
    elif user_input == 'n':
        print("thank you")
    else:
        return answer()
       

if __name__ == "__main__":
    main()
