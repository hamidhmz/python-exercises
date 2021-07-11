"""exceptions"""
# https://docs.python.org/3/library/exceptions.html
# ---------------------------------------------------------------------------- #
#                                   handling                                   #
# ---------------------------------------------------------------------------- #
# ------------------------------- first example ------------------------------ #
try:
    age = int(input('age: '))
except ValueError as so:
    print(ValueError)
    print(so)
else:
    print('without exceptions')
finally:
    print('done with or without error')


# ------------------------------ seconnd example ----------------------------- #
try:
    age = int(input('age: '))
    XFACTOR = 10/age
except ValueError as myError:
    print(ValueError)
    print(myError)
except ZeroDivisionError as myError:
    print(ZeroDivisionError)
    print(myError)
else:
    print('without exceptions')


# ------------------------------- third example ------------------------------ #
try:
    age = int(input('age: '))
    XFACTOR = 10/age
except (ValueError, ZeroDivisionError) as myError:
    print(myError)
else:
    print('without exceptions')


# ---------------------------------------------------------------------------- #
#                                    raising                                   #
# ---------------------------------------------------------------------------- #
def calculate_xfactor(age_1):
    """calculate_xfactor"""
    if age_1 <= 0:
        raise ValueError('age cannot be 0 or less')
    return 10/age_1
