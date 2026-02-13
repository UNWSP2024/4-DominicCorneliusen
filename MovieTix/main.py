#Title: Movie Tix
#Author: Dominic Corneliusen
#Date last modified: 2/13/2026

#Variables
count = int(input("How many movies would you like to watch in theatres in the next year?"))
movies = count
totalTickets = 0
#While loop
while count > 0:
    input("What is the movie title?")
    ticketsPerMovie = int(input("How many tickets would you like for this movie?"))
    totalTickets = ticketsPerMovie + totalTickets
    count -= 1
#Final Print statement
print("You would like to see", movies, "movies in theatres in the next year."
        " You want", totalTickets, "tickets in total for movies this year.")
