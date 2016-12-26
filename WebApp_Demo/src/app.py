
def prompt_age():
    user_age = raw_input("Enter your age: ")
    age_seconds = int(user_age) * 365 * 24 * 60 * 60

    print("Your age is {} seconds.".format(age_seconds))

prompt_age()