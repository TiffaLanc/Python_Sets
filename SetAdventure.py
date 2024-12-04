# Task 1: Flight Route Comparison Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. You have two sets of flight destinations
# , one for each airline. Write a Python program to find out:

# 1. Destinations that both airlines fly to.

# 2. Destinations unique to your airline.

# 3. Whether there are any destinations that neither airline shares.



our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

def same_route(airline1, airline2):
    same_routes = airline1.intersection(airline2)
    print("Both airlines fly to these destinations: " ,same_routes)

def my_route(airline1, airline2):
    my_routes = airline1.difference(airline2)
    print("My airline flies to these destinations: " , my_routes)

def unique_route(airline1, airline2):
    unique_routes = airline1.symmetric_difference(airline2)
    if unique_routes:
        print("These are destinations niether airline shares: ", unique_routes)
    else:
        print("Both airlines fly to these destinations.")

routes = same_route(our_routes, competitor_routes)
routes = my_route(our_routes, competitor_routes)
routes = unique_route(our_routes, competitor_routes)
