print("Just don't ask")
list_of_things = ["Me", "Nothing else"]
def dev():
    return 0 / 0
if list_of_things[0] == "Me":
    try:
        dev()
    except:
        while list_of_things[1] == "Nothing else":
            print("forever")
