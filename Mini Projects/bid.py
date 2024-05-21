import sys

bid_history = {}
repeat = "Yes"

while repeat == "Yes":
    name = input("what is your name: ")
    bid = int(input("What is your bid: ₹"))

    bid_history[name] = bid

    repeat = input("Are there any bidders for bidding 'Yes' or 'No': ")


max_bid = -sys.maxsize -1
for key in bid_history:
    if bid_history[key] > max_bid:
        max_bid = bid_history[key]
        winner = key

print(f"The winner is {winner} with the bid of ₹{max_bid}")
