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
            movies[movie]["booked_user"].add(user)
            print(f"ticker booked for user {user} for the movie '{movie}'.")
        else:
            print(f"sorry, {movie} sold out. ")
    else:
        print("Movie not found.")   

def cancel_boking(user,movie):
    if movie in movies:
