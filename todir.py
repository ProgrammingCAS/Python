def inputEx(prompt):
    var = input(prompt)
    print("\033[1A", end='')
    print(' ' * (len(prompt) + 50), end='\r') 
    return var
def todir_f(todir, var):
    j = 0
    list = todir.split()
    print(f'{var} = [', end='')
    for i in list:
        if i == " ":
            pass
        else:
            print(f'"{i}", ', end='')
            if j == len(list) - 1:
                print(f'"{i}"]', end='')
        j+=1
def main():
    todir = inputEx("List|> ")
    var = inputEx("Name|> ")
    todir_f(todir, var)
if __name__ == "__main__":
    main()
