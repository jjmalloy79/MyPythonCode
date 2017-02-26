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
def userList(prompt):
    print prompt,
    l= raw_input().split(",")
    return l
    
def userInt(prompt):
    print prompt,
    num = int(raw_input())
    return num
    
def userString(prompt):
    print prompt,
    s = raw_input()
    return s
    
def userFloat(prompt):
    print prompt,
    f = float(raw_input())
    return f
      
def kmToMi(km):
    return 0.62 * km