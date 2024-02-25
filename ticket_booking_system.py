class Movie:
    def init(self, name, preference, seat):
        self.name = name
        self.preference = preference
        self.seat = seat

    def registration(self):
        name = input("Enter your name: ")
        pref = int(input("Enter the number according to your preference: "))
        seat = int(input("Enter number of seats you want to book: "))
        fare = self.preference[pref] * seat
        print("Total fare before update:", fare)
        
        # Update fare based on user preference
        update_pref = input("Do you want to update your preference? (yes/no): ")
        if update_pref.lower() == "yes":
            new_pref = int(input("Enter the new preference number: "))
            fare = self.preference[new_pref] * seat
            print("Total fare after update:", fare)
        else:
            print("Total fare remains unchanged.")
        
        return fare

    @staticmethod
    def show_timings():
        print("Morning shows: 10:00 am, 12:00 pm")
        print("Noon shows: 2:00 pm, 5:00 pm")
        print("Night shows: 8:30 pm, 11:30 pm")

# Dictionary to store price preferences
preference = {1: 180, 2: 160, 3: 120, 4: 80}

while True:
    print("Welcome to the online ticket booking system")
    print("1. Show timings")
    print("2. Book tickets")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        Movie.show_timings()
    elif choice == 2:
        movie = Movie(None, preference, None)  # Create a movie object
        print("Please enter details for ticket booking:")
        fare = movie.registration()
        print("Total fare:", fare)
    elif choice == 3:
        print("Thank you for using our ticket booking system")
        break
    else:
        print("Invalid choice. Please choose again.")
#simpe_movie_booking_system_using_oops
