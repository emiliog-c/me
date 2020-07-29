# -*- coding: UTF-8 -*-
"""Refactoring.

This exercise contains a complete and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

Some functions will have directions as external comments, once you think you
are on top of it, take these comments out. Others won't have comments and
you'll need to figure out for yourself what to do.
"""
import requests

# This is a terrible function. The rest of the functions in this file do a
# much better job of what it's trying to do. Once you've has a little look,
# move on, and eventually delete this function. (And this comment!)
def do_bunch_of_bad_things():
#    print("Getting ready to start in 8")
#    print("Getting ready to start in 7")
#    print("Getting ready to start in 6")
#    print("Getting ready to start in 5")
#    print("Getting ready to start in 4")
#    print("Getting ready to start in 3")
#    print("Getting ready to start in 2")
#    print("Getting ready to start in 1")
#    print("Let's go!")
#
#    triangle = {"base": 3, "height": 4}
#    triangle["hypotenuse"] = triangle["base"] ** 2 + triangle["height"] ** 2
#    print("area = " + str((triangle["base"] * triangle["height"]) / 2))
#    print("side lengths are:")
#    print("base: {}".format(triangle["base"]))
#    print("height: {}".format(triangle["height"]))
#    print("hypotenuse: {}".format(triangle["hypotenuse"]))
#
#    another_hyp = 5 ** 2 + 6 ** 2
#    print(another_hyp)
#
#    yet_another_hyp = 40 ** 2 + 30 ** 2
#    print(yet_another_hyp)
    


# return a list of countdown messages, much like in the bad function above.
# It should say something different in the last message.
    pass
def countdown(message, start, stop, completion_message):
    cd = []
    for i in range (start, stop):
        ce = ((message) + (i))
        cd.append(ce)
        print(ce)
    cd.append(completion_message)
    cd.append("AHHHH")
    print((cd))
    return cd



# TRIANGLES

# This should be a series of functions that are ultimatly used by
# triangle_master
# It should eventually return a dictionary of triangle facts. It should
# optionally print information as a nicely formatted string. Make printing
# turned off by default but turned on with an optional argument.
# The stub functions are made for you, and each one is tested, so this should
# hand hold quite nicely.
def calculate_hypotenuse(base, height):
    import math
    print (base)
    print (height)
    initial = ((base) ** 2 + (height) ** 2)
    hypotenuse = math.sqrt(initial)
    return hypotenuse



def calculate_area(base, height):
    initial = ((base * (height)))
    area = (initial/2)
    return area



def calculate_perimeter(base, height):
    import math
    initial = ((base) ** 2 + (height) ** 2)
    hypotenuse = math.sqrt(initial)
    perimeter = ((base) + (height) + (hypotenuse))
    return perimeter



def calculate_aspect(base, height):
    t = False
    while t != True:
        if height > base:
            aspect = ("tall")
            t = True
        elif base > height:
            aspect = ("wide")
            t = True
        else:
            aspect = ("equal")
            t = True
    return aspect


# Make sure you reuse the functions you've already got
# Don't reinvent the wheel
def get_triangle_facts(base, height, units="mm"):
    return {
        "area": calculate_area(base, height),
        "perimeter": calculate_perimeter(base, height),
        "height": ((height)),
        "base": ((base)),
        "hypotenuse": calculate_hypotenuse(base, height),
        "aspect": calculate_aspect(base, height),
        "units": (units),
    }



# this should return a multi line string that looks a bit like this:
#
# 15
# |
# |     |\
# |____>| \  17.0
#       |  \
#       |   \
#       ------
#       8
# This triangle is 60.0mm²
# It has a perimeter of 40.0mm
# This is a tall triangle.
#
# but with the values and shape that relate to the specific
# triangle we care about.
def tell_me_about_this_right_triangle(facts_dictionary):
    tall = """
            {height}
            |
            |     |\\
            |____>| \\ <-{hypotenuse}
                  |  \\
                  |   \\
                  ------
                  {base}"""
    wide = """
            {hypotenuse}
             ↓         ∕ |
                   ∕     | <-{height}
               ∕         |
            ∕------------|
              {base}"""
    equal = """
            {height}
            |
            |     |⋱
            |____>|  ⋱ <-{hypotenuse}
                  |____⋱
                  {base}"""

    pattern = (
        "This triangle is {area}{units}²\n"
        "It has a perimeter of {perimeter}{units}\n"
        "This is a {aspect} triangle.\n"
    )

    facts = pattern.format(
        **facts_dictionary
    )  # **dictionary unpacks the key value pairs


def triangle_master(base, height, return_diagram=False, return_dictionary=False):
    dictionary_tri_fact = get_triangle_facts(base, height, units="mm")
    diagram = tell_me_about_this_right_triangle(dictionary_tri_fact)

    if return_diagram and return_dictionary:
        return {"diagram": diagram, "dictionary": dictionary_tri_fact}
    elif return_diagram:
        return diagram
    elif return_dictionary:
        return dictionary_tri_fact
    else:
        print("You're an odd one, you don't want anything!")


def wordy_pyramid():
    wp = list(range(3, 21, 2))
    wp.extend(list(range(20, 3, -2)))
    wLengths = wp
    words = list_of_words_with_lengths(wLengths)
    return words


def get_a_word_of_length_n(length):

    baseURL = (
        f"https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={length}"
    )
    url = baseURL.format(length)
    r = requests.get(url)
    if r.status_code is 200:
        message = r.text
        return message
    else:
        print("failed a request", r.status_code)

def list_of_words_with_lengths(list_of_lengths):
    list_of_words = []
    for i in list_of_lengths:
        list_of_words.append(get_a_word_of_length_n(i))

    return list_of_words

if __name__ == "__main__":
    do_bunch_of_bad_things()
    countdown("We're about to start", 9, 1, "we finished, wheeeee!")
    triangle_master(3, 5)
    pyramid = wordy_pyramid()
    for word in pyramid:
        print(word)
