# -*- coding: UTF-8 -*-
"""
I'm in UR exam.
This is the same as the weekly exercises, fill in the functions,
and test them to see if they work.
You have 2 hours.
"""
import string
import time


def string_please() -> str:
    """Returns a string, anything you like."""
    return str("This Test")


def list_please() -> list:
    """Returns a list, anything you like."""
    a = [2,3,4,5]
    return a


def dictionary_please() -> dict:
    """Returns a dictionary, anything you like."""
    dictionary = {"Big": "Bruh", "Lets": "Go"}
    return dictionary


def is_it_5(some_number) -> bool:
    """Returns True if the argument passed is 5, otherwise returns False."""
    well_is_it = False
    if (some_number) == 5:
        well_is_it = True
        return well_is_it
    else:
        return well_is_it


def take_five(some_number) -> int:
    """Subtracts 5 from some_number."""
    c = (some_number) - 5
    return c


def greet(name="Towering Timmy"):
    """Return a greeting.
    return a string of "Hello " and the name argument.
    E.g. if given as "Towering Timmy" it should return "Hello Towering Timmy"
    """
    return ("Hello " + (name))


def three_counter(input_list=[1, 4, 3, 5, 7, 1, 3, 2, 3, 3, 5, 3, 7]):
    """Count the number of 3s in the input_list.
    Return an integer.
    TIP: the test will use a different input_list, so don't just return 5
    """
    count = input_list.count(3)
    return count


def n_counter(search_for_this, input_list=[1, 4, 3, 5, 7, 1, 3, 2, 3, 3, 5, 3, 7]):
    """Count the number of times search_for_this shows up in the input_list.
    Return an integer.
    """
    init = input_list.count(search_for_this)
    count = int(init)
    return count


def fizz_buzz():
    """Do the fizzBuzz.

    This is the most famous basic programming test of all time!
       "Write a program that prints the numbers from 1 to 100. But for
        multiples of three print "Fizz" instead of the number and for
        the multiples of five print "Buzz". For numbers which are
        multiples of both three and five print "FizzBuzz"."
    from https://blog.codinghorror.com/why-cant-programmers-program/
    
    Return a list that has an integer if the number isn't special, 
    and a string if it is. E.g. 
        [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 
         'Fizz', 'Buzz',  11, 'Fizz', 13, 14, 
         'FizzBuzz', 16, 17, ...]
    """
    fizzBuzzList = []
    # your code here
    for i in range (1, 101):
        if i % 3 == 0 and i % 5 == 0:
            fizzBuzzList.append("FizzBuzz")
        elif i % 3 == 0:
            fizzBuzzList.append("Fizz")
        elif i % 5 == 0:
            fizzBuzzList.append("Buzz")
        else:
            fizzBuzzList.append(i)
    return fizzBuzzList


def put_behind_bars(input_string="very naughty boy"):
    """Interleave the input_string with pipes.
    Given any string, interleave it with pipes (| this character)
    e.g. "very naughty boy" should return the string
    "|v|e|r|y| |n|a|u|g|h|t|y| |b|o|y|"
    TIP: strings are pretty much lists of chars. 
         If you list("string") you get ['s', 't', 'r', 'i', 'n', 'g']
    TIP: consider using the 'join' method in Python.
    TIP: make sure that you have a pipe on both ends of the string.
    """
    x = list(input_string)
    j = "|".join(x)
    print (j)
    p = ("|" + j + "|")
    print (p)
    return p


def pet_filter(letter="a"):
    """Return a list of pets whose name contains the character 'letter'"""
    # fmt: off
    pets = [
            "dog", "goat","pig","sheep","cattle","zebu","cat","chicken",
            "guinea pig","donkey","duck","water buffalo","western honey bee",
            "dromedary camel","horse","silkmoth","pigeon","goose","yak",
            "bactrian camel","llama","alpaca","guineafowl","ferret",
            "muscovy duck","barbary dove","bali cattle","gayal","turkey",
            "goldfish","rabbit","koi","canary","society finch","fancy mouse",
            "siamese fighting fish","fancy rat and lab rat","mink","red fox",
            "hedgehog","guppy",]
    # fmt: on
    filtered = []
    a = (letter)
    filt = [s for s in pets if (a) in s]
    filtered.extend(filt)
    print (filtered)
    return filtered


def best_letter_for_pets():
    """Return the letter that is present at least once in the most pet names.
    Reusing the pet_filter, find the letter that gives the longest list of pets
    TIP: return just a letter, not the list of animals.
    """
    import string

    the_alphabet = string.ascii_lowercase
    pets = [
            "dog", "goat","pig","sheep","cattle","zebu","cat","chicken",
            "guinea pig","donkey","duck","water buffalo","western honey bee",
            "dromedary camel","horse","silkmoth","pigeon","goose","yak",
            "bactrian camel","llama","alpaca","guineafowl","ferret",
            "muscovy duck","barbary dove","bali cattle","gayal","turkey",
            "goldfish","rabbit","koi","canary","society finch","fancy mouse",
            "siamese fighting fish","fancy rat and lab rat","mink","red fox",
            "hedgehog","guppy",]
    j = 0
    filtered = []
    b = list(the_alphabet)
    while j != 25:
        filtered = []
        letter = b[j]
        filt = [s for s in pets if letter in s]
        filtered.append(filt)
        c=len(filt)
        print (filtered)
        print(c)
        j = j+1
    popular_letter = "e"

    return popular_letter


def make_filler_text_dictionary():
    """Make a dictionary of random words filler text.
    There is a random word generator here:
    https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength=4 
    If we set minLength=18 and maxLength=18, we will get something like this:
    >>> url = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength=18"
    >>> r = requests.get(url)
    >>> r.text # will get you a string, something like this:
    >>> "occipitosphenoidal"
    
    Return a dictionary where the keys are numbers, and the values are lists of
    words. e.g.
    { 
        3: ['Sep', 'the', 'yob'],
        4: ['aaaa', 'bbbb', 'cccc'],
        ...
        7: ['aaaaaaa', 'bbbbbbb', 'ccccccc']
    }
    Use the API to get the 3 words.
    
    The dictionary should have the numbers between 3 and 7 inclusive.
    (i.e. 3, 4, 5, 6, 7 and 3 words for each)
    TIP: you'll need the requests library
    """

    import requests
    num = 3
    url = ("https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength="+str(num))
    wd = {}
    exlist = []
    while num != 8:
        exlist = []
        for i in range(0,3):
            url = ("https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength="+str(num))
            r = requests.get(url)
            msg = r.text
            exlist.append(msg)
        wd[(num)] = (exlist) 
        num = num + 1

    return wd


def random_filler_text(number_of_words=200):
    """Make a paragraph of random filler text.
    Using the dictionary returned by make_filler_text_dictionary, make a
    paragraph of text using randomly picked words. Each word should be a random
    length, and a random one of the 3 words.
    Make the paragraph have number_of_words words in it.
    Return it as a string
    TIP: you'll need the random library, 
        see line 77 of week4/hangman_leadboard.py for an example.
    """
    import random

    my_dict = make_filler_text_dictionary()
    words = []
    realNum = number_of_words//5
    for i in range(0, (realNum)):
        jay = [random.choice(i) for i in my_dict.values()]
        words.extend(jay)

    return " ".join(words)


def fast_filler(number_of_words=200):
    """Reimplement random_filler_text.
    This time, the first time the code runs, save the dictionary returned
    from make_filler_text_dictionary to a file.
    On the second run, if the file already exists use it instead of going to
    the internet.
    Use the filename "dict_racey.json"
    TIP: you'll need the os and json libraries
    TIP: you'll probably want to use json dumps and loads to get the 
    dictionary into and out of the file. Be careful when you read it back in, 
    it'll convert integer keys to strings.
    If you get this one to work, you are a Very Good Programmer™!
    """
    import random
    import os
    import json

    # Keep presets
    words = []
    test = {3: ['iof', 'ead', 'zac'], 4: ['yont', 'iiwi', 'qadi'], 5: ['ygapo', 'yonic', 'yaply'], 6: ['yodels', 'ipecac', 'ygerne'], 7: ['iffiest', 'ipocras', 'ipomoea']}
    fname = "dict_racey.json"
    path = (r"C:\Users\Emilio\1161\me\dict_racey.json")
    exists = os.path.isfile(path)
    if exists != True:
        with open (fname, "w") as fp:
            json.dump(test, fp)
        with open (fname) as fp:
            j = json.load(fp)
        new_d = {}
        for k,v in j.items():
            try:
                new_d[int(k)] = v
            except ValueError:
                new_d[k] = v
        realNum = number_of_words//5
        print (new_d)
        for i in range(0, (realNum)):
            jay = [random.choice(i) for i in new_d.values()]
            words.extend(jay)
            
    else:
        with open (fname, "r") as fp:
            j = json.load(fp)
        new_d = {}
        for k,v in j.items():
            try:
                new_d[int(k)] = v
            except ValueError:
                new_d[k] = v
        realNum = number_of_words//5
        print (new_d)
        for i in range(0, (realNum)):
            jay = [random.choice(i) for i in new_d.values()]
            words.extend(jay)
            
    wordz = " ".join(words)  
    wfinal = wordz.capitalize() + "."
    return wfinal


if __name__ == "__main__":
    print("string_please", type(string_please()) == str)
    print("list_please", type(list_please()) == list)
    print("dictionary_please", type(dictionary_please()) == dict)
    print("is_it_5", is_it_5(5))
    print("is_it_5", is_it_5(6))
    print("take_five", take_five(5))
    print("take_five", take_five(3))
    print("greet:", greet())
    print("three_counter:", three_counter())
    print("n_counter:", n_counter(7))
    print("fizz_buzz:", fizz_buzz())
    print("put_behind_bars:", put_behind_bars())
    print("pet_filter:", pet_filter())
    print("best_letter_for_pets:", best_letter_for_pets())
    print("make_filler_text_dictionary:", make_filler_text_dictionary())
    print("random_filler_text:", random_filler_text())
    print("fast_filler:", fast_filler())
    for i in range(10):
        print(i, fast_filler())
    print(
        "These are mini tests, they show you some output.",
        "\nDon't forget to run the real tests.",
        "\nThey test your code against the non-default arguments",
    )
