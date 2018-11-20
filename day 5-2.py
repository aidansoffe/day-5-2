is_male=False
if is_male:
    print("You are a man")
else:
    print("You are not a man")

is_male=True
is_tall=True


if is_male or is_tall:
    print("you are a male or tall or both")
else:
    print("you are neither a male or tall")

is_male= True
is_tall=True

if is_male and is_tall:
    print("you are a tall man")
elif is_male and not (is_tall):
    print("you rae a short man")
elif not (is_male) and is_tall:
    print("you are not a male but tall")
else:
    print("you are either not male or tall or both")