starting_speed = 0
acceleration = 0
end_speed = 0
def get_distance():
    starting_speed = float(input("Starting Speed (m/second): "))
    end_speed = float(input("End Speed (m/second): "))
    acceleration = float(input("Acceleration (m/second^2): "))
    end_start = (end_speed * end_speed) - (starting_speed * starting_speed)
    distance = end_start/(2 * acceleration)
    return str(distance)
def main(): 
    distance = get_distance()
    print(f"{distance}m travelled")
    again = input("New vars? ")
    if again == "yes" or again == "y":
        print("starting again...")
        main()
    # (endspeed^2 - startingspeed^2)/2accleration
    
main()
