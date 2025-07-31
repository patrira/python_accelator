def bill_split(amount, friends):
    amount= int(input("Please Enter the amount to spilt the Billl: "))
    friends =int(input(" Enter also the number of your freinds: "))

    total_bill_with_tax = amount + ((amount * 20)/100)
    bill_per_friend = total_bill_with_tax /friends
    print("Total to be paid by single friend: ", bill_per_friend)

bill_split(200000, 35)  