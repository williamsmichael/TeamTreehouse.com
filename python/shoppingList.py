# add items to the list
# type QUIT to stop running the list collection
# display the list

listing = []
status = True
while status:
    item = input("Input an item ['DONE' to see list]: ").lower()
    if item == "DONE".lower():
        status = False
    else:
        listing.append(item)

print("\nHere is your list:")
for item in listing:
    print(item)