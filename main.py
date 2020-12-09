from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)
keepBiding = True
auction = {}

def highest_bidder(bidding_record):
  highest_bid = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ₹{highest_bid}")



while keepBiding:
  name = input("What is your name? ")
  bid = int(input("What's your bid? ₹"))

  auction[name] = bid

  ask = input("Are there any other bidders? Type 'yes' or 'no': ")
  if ask == "yes":
    clear()
  elif ask == "no":
    keepBiding = False
    highest_bidder(auction)
  
  




