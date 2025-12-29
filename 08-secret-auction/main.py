from art import logo
print(logo)

def highest_bid(bids):
    maxi_bid=0
    winner=""
    for key in bids:
        bid_amt = bids[key]
        if bid_amt > maxi_bid:
            maxi_bid = bid_amt
            winner = key
    print(f"The winner is {winner} with a bid of ${maxi_bid}")

bid={}
cont_bid=True

while cont_bid :
    name = input("What is your name? :")
    amt = int(input("What is your bid? : $"))
    bid[name]=amt
    cont = input("Are there any other  bidders? Type 'yes or no': ").lower()
    if cont=="no":
        cont_bid=False
        highest_bid(bid)
    elif cont == "yes":
        print("\n" * 20)





















# def highest_bidder(bidding_rec):
#     highest_bid = 0
#     winner = ""
#     for bid in bidding_rec:
#         bid_amt = bidding_rec[bid]
#         if bid_amt > highest_bid:
#             highest_bid = bid_amt
#             winner = bid
#     print(f"The winner is {winner} with the highest bid of ${highest_bid} 💐")
#
# bids={}
# continue_bid=True
# while continue_bid:
#     name = input("What is your name?\n")
#     price = int(input("What is your bid?\n"))
#     bids[name] = price
#     ans=input("Are there any other bidders? Type 'yes or 'no'.\n")
#     if ans=="no":
#         continue_bid=False
#         highest_bidder(bids)
#     elif ans=="yes":
#         print("\n" * 20)
