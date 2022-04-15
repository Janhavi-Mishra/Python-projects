from replit import clear
import art
#flow - create nested dictionary, loop and add input, loop and check bid, return highest bid

#print logo
print(art.logo)

#empty dictionary
bidders = {}

#fuction to add to dictionary
def bidders_info(bidder_name, bid_value):
    new_name = bidder_name
    new_bid = float(bid_value) 
    bidders[new_name] = new_bid

#function to check highest bid
def highest_bid(bidding_record):
    max_value = 0
    winner_name = ""
    for bidder in bidding_record:
        if bidders[bidder] > max_value:
            max_value = bidders[bidder]
            winner_name = bidder
    print(f"\nThe winner is {winner_name} with a bid of ${max_value}")

#flag value to check if continue
flag_value = "yes"

#loop to continue if flag true
while flag_value == "yes":
    name = input("What is your name? ")
    bid = float(input("\nHow much do you want to bid? $"))
    bidders_info(name,bid)
    flag_value = input("\nAre there more bidders? Type yes or no: ").lower()
    clear()
    #print logo
    print(art.logo)

highest_bid(bidders)
