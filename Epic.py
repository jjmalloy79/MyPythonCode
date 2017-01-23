# gets a users input for a string
def get_input(prompt):
    print prompt
    s = raw_input()
    return s
    
# gets a users input for a int
def get_int(prompt):
    print prompt
    num = int(raw_input())
    return num
    
#removes cookies
def remove_cookie(s):
# this sees if cookies is in string
    s = s.upper()
    if s.find("COOKIES") != -1:
# if cookies is in the string it replaces it
        s = s.replace("COOKIES", "_______")
    return s
