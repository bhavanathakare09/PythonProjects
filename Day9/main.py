# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


import art
print(art.logo)

new_bid = True
bidders = {
}

def highest_bid(bidders_dict):
    max_value = 0
    winner =""
    for key in bidders_dict:
        if bidders_dict[key] > max_value:
            max_value = bidders_dict[key]
            winner = key
    print(f"The winner is {winner} with a bid of $ {max_value}")

while new_bid:
    name = input("Enter your name? : ").lower()
    bid_value = int(input("what is your bid?: $"))
    bidders[name] = bid_value
    input_rerun = True
    while input_rerun:
        next_bidder = input("Are there any other bidders? Type 'Yes' or 'No': ").lower()
        if next_bidder in ["yes", "no"]:
            input_rerun = False
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")
    # next_bidder = input("Are there any other bidder? Type 'Yes' or 'No' .").lower()

    if next_bidder == "no":
        new_bid = False
        highest_bid(bidders)
    elif next_bidder == "yes":
        print("\n"*20)
    else:
        print("Please provide correct option as 'Yes' or 'No' :")
        break




