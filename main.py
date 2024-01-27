Accounts = [["robin", "da bank"]]
Status = []


def signup(un, pw):
    csu = True
    # loop existing accounts
    for A in Accounts:
        # A[0] reperesentsd
        if un == A[0]:
            print("username here already sucky")
            csu = False

    if (csu):
        Accounts.append([un, pw])

    menu()


def login(un, pw):
    loggedin = False
    for A in Accounts:
        if (A[0] == un and A[1] == pw):
            print("logged in")
            loggedin = True
            submenu()

    if (loggedin == False):
        print("Login unsuccessful")


def post():
    pppp = input("what would you like to post???")
    Status.append(pppp)
    print("Posting status: " + pppp)
    submenu()


def submenu():
    print("choose an option")
    print("1. post a status")
    print("2. veiw all statuses")
    print("3. edit a status")
    print("4. delete a status")

    ppp = input("pick a option")
    if (ppp == "1"):
        print("your posting a status")
        post()
    elif (ppp == "2"):
        print("your veiwing a status")
    elif (ppp == "3"):
        print("your editing a status")
    elif (ppp == "4"):
        print("your delteting a status")
    else:
        print("sucky")


def menu():
    print("Welcome to that 1 game")
    pp = input("you want sign up or log in??? ")
    if (pp == "sign up"):
        un = input("pls give us ur name ingame ")
        pw = input("pls give us ur password ")
        signup(un, pw)
    elif (pp == "log in"):
        un = input("pls give us ur name ingame ")
        pw = input("pls give us ur password ")
        login(un, pw)
    else:
        print("wut sucky")


menu()