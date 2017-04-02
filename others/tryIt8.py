import Epic

def main():
    l = Epic.userList("Enter three numbers, each separated by a common:  ")
    for n in l:
        for i in range(0, int(n)):
            print n,
        print
main()