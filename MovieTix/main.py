#Title: Movie Tix
#Author: Dominic Corneliusen
#Date last modified: 2/13/2026
'''
Write a program that has the user input various movie names and
how many tickets are desired for each movie.  At the end of the
program it prints out the total number of tickets desired by the
user.  Use either a "for loop" or "while loop" to accomplish this.'''

#Variables
count = int(input("How many movies would you like to watch in theatres in the next year?"))
movies = count
totalTickets = 0
while count > 0:
    input("What is the movie title?")
    ticketsPerMovie = int(input("How many tickets would you like for this movie?"))
    totalTickets = ticketsPerMovie + totalTickets
    count -= 1

print("You would like to see", movies, "movies in theatres in the next year."
        " You want", totalTickets, "tickets in total for movies this year.")