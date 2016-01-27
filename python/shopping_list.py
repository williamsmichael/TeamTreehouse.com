# add items to the list
# type QUIT to stop running the list collection
# display the list

def main():
    
    listing = []
    status = True
    
    def instructions():
        # display instuctions
        print("\nWhat should we pick-up at the store?")
        print("'DONE' to stop adding items.")
        print("'HELP' to see these instructions.")
        print("'SHOW' to see your list.\n")
        
    def show_listing():
        # show the list
        if len(listing) == 0:
            print("-- EMPTY --")
        else:
            print("\nHere is your list of {} item(s):".format(len(listing)))
            for item in listing:
                print("-", item)
        print("")
        
    def add_item(item):
        # add an item to the list
        listing.append(item)
        print("Added {}. List now has {} item(s).\n".format(item, len(listing)))
    
    # interacts with the user to get list items
    instructions()
    while status:
        # collect user input do an action
        # the alternative is break and continue to prevent calling add_item
        item = input("Input an item: ").lower()
        if item == "DONE".lower():
            status = False
        elif item == "HELP".lower():
            instructions()
        elif item == "SHOW".lower():
            show_listing()
        else:
            add_item(item)
    
    show_listing()
    
if __name__ == "__main__":
    main() 