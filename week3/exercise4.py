# -*- coding: UTF-8 -*-
"""Week 3, Exercise 4."""


import math
import bisect
# import time


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.
    
    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}
    
    This will be quite hard, especially hard if you don't have a good diagram!
    
    Use the VS Code debugging tools a lot here. It'll make understanding 
    things much easier.
    """
    ai = low
    ae = high
    ad = (actual_number)
    arr = list(range (ai, ae))
    def wack(arr, ai, ae, ad):
        tries = 0
        guess = 0
        df = False
        while df != True:
            if ai >= 1:
                mid = ai + (ae - ai)//2
                if arr[mid] == ad:
                    print (mid)
                    guess = mid
                    print (guess)
                    print (tries)
                    df = True
                    return mid

                elif arr[mid] > ad:
                    wrongguess = (mid)
                    print (wrongguess)
                    tries = tries + 1
                    return wack(arr, ai, mid-1, ad)
                else:
                    wrongguess2 = (mid)
                    print (wrongguess2)
                    tries = tries + 1
                    return wack(arr, ae, mid+1, ad)
        return {"guess": guess, "tries": tries}


if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
