# happy.py
# This program say happy birthday to Fred, Lucy, and Elmer
# Writen by: Ali Arefi

def happy():
    print("Happy bithday to you!")

def sing(person):
    happy()
    happy()
    print("Happy birthday, dear", person + ".")
    happy()

def main():
    sing("Fred")
    print()
    sing("Lucy")
    print()
    sing("Elmer")

main()
