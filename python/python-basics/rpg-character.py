full_dot = '●'
empty_dot = '○'

def create_character(name, force, intelligence, carism):
    if not isinstance(name, str):
        return "The character name should be a string"
    elif name == "":
        return "The character should have a name"
    elif len(name) > 10:
        return "The character name is too long"
    elif " " in name:
        return "The character name should not contain spaces"
    elif not isinstance(force, int) or not isinstance(intelligence, int) or not isinstance(carism, int):
        return "All stats should be integers"
    elif force < 1 or intelligence < 1 or carism < 1:
        return "All stats should be no less than 1"
    elif force > 4 or intelligence > 4 or carism > 4:
        return "All stats should be no more than 4"
    elif force + intelligence + carism != 7:
        return "The character should start with 7 points"
    else:
        return f"""{name}
STR {full_dot * force + empty_dot * (10 - force)}
INT {full_dot * intelligence + empty_dot * (10 - intelligence)}
CHA {full_dot * carism + empty_dot * (10 - carism)}"""

create_character('ren', 4, 2, 1)
print(create_character('ren', 4, 2, 1))