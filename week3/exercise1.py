# -*- coding: UTF-8 -*-
"""Week 3.

Modify each function until the tests pass.
"""


def loop_ranger(start, stop=None, step=1):
    """Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from JUST using range()
    The look up the docs for range(), you can answer this with just the range 
    function, but we'd like you to do it the long way, probably using a loop.
    """
    numbers = []
    y = start
    while y < stop:
        numbers.append(y)
        y = y + step

    return numbers


def lone_ranger(start, stop, step):
    """Duplicate the functionality of range.

    Look up the docs for range() and wrap it in a 1:1 way
    """
    nom = []
    while start < stop:
        nom.append(start)
        start = start + step
    
    return nom


def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2
    """
    a1 = start
    a2 = stop
    a3 = 2
    step_range = []
    for number in range (a1, a2, a3):
        step_range.append(number)

    return step_range


def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK

    Look up the docs for input
    """
    duh = int(input("What number is between low and high? "))
    while not (low < duh < high):
        if duh < low:
            print ('Higher.')
        if duh > high:
            print ('Lower')
        if duh > low and duh < high:
            print ("nah")
            return duh
        duh = int(input("What number is between low and high? "))
  
    return duh


def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number 
    (e.g. "cow", "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    exe1 = input("What number is between low and high? ")
    while not exe1.isdigit():
        exe1 = input(message)
        return exe1

    return exe1
    


def super_asker(low, high):
    """Robust asking function.

    Combine what you learnt from stubborn_asker and not_number_rejector
    to make a function that does it all!
    Try to call at least one of the other functions to minimise the
    amount of code.
    """
    message = ("put a number ")
    tf = False
    exe2 = input("What number is between low and high? ")
    while tf != True:
        while not exe2.isdigit():
            exe2 = input("bruh ")
            return exe2
            while not (low < exe2 < high):
                if exe2 < low:
                    print ('Higher.')
                if exe2 > high:
                    print ('Lower')
                if exe2 > low and exe2 < high:
                    print ("nah")
                    tf = True
                    return exe2
        

    return exe2


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\nlone_ranger", lone_ranger(1, 10, 3))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector("Enter a number: ")
    print("\nsuper_asker")
    super_asker(33, 42)
