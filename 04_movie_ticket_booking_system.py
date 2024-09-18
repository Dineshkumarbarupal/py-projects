# View available movies.
# Book tickets for a movie.
# Check how many tickets are available for each movie.
# Cancel a booking.
# Exit the system


movies = {
    "movie1":{"ticket":5,"booked_users": set()},
    "movie2":{"ticket":5,"booked_users": set()},
    "movie3":{"ticket":5,"booked_users": set()}
}


def display_movies():
    print("/n Availbale Movie---")
    for movie,info in movies.items():
        print(f"{movie}:{info["ticket"]} Tickets Avaible")
    

def book_ticket(user,movie):
    if movie in movies:
        if movies[movie]["ticket"] > 0:
            movies[movie]["ticket"] -= 1
            movies[movie]["booked_users"].add(user)
            print(f"ticker booked for user {user} for the movie '{movie}'.")
        else:
            print(f"sorry, {movie} sold out. ")
    else:
        print("Movie not found.")   

def cancel_boking(user,movie):
    if movie in movies:
        if user in movies[movie][f"booked_user"]:
            movies[movie]["ticket"] += 1
            movies[movie]["booked_users"].remove(user)
            print(f"Booking cancelled for {movie} for {user}")
        else:
            print(f"{user} has not booked any ticket for {movie} ")  
    else:
        print("movie not found")

def manu():
    while True:
        print("/n...movie ticket booking system")
        print("1, View Available Movie ")
        print("2,  book a ticket")
        print("3, cancel movie ticket")
        print("4, Exit")

        choise = input("Enter your choise: ")

        if choise == "1":
            display_movies()

        elif choise == "2":
            user = input("Enter your name:")
            movie = input("Enter movie name:")
            book_ticket(user,movie)

        elif choise == "3":
            user = input("Enter your name:")
            movie = input("Enter movie name:")
            cancel_boking(user,movie)

        elif choise == "4":
            print("Exit the system.")
            break
        else:
            print("invalid choise, please try again.")
manu()            
