##Exercise1
inventory = {
    'gold' : 500,
    'pouch' : ['flint','twine', 'gemstone'],
    'blackpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
inventory['pocket'] = ["seashell", "strange berry", "lint"]

inventory['blackpack'].sort()

inventory['blackpack'].remove("dagger")

inventory["gold"] += 50



##Exercise2
prices={}

prices["banana"]=4
prices["apple"]= 2
prices["orange"]= 1.5
prices["pear"]= 3

stock={}

stock["banana"]= 6
stock["apple"]= 0
stock["orange"] =32
stock["pear"]= 15

for food in prices:
    print(food)
    print("price: ",prices[food])
    print("stock: ", stock[food])

total=0
for price in prices:
    money= prices[price]*stock[price]
    print(money)
    total=total +money
    print("The total money is", total)


##Exercise3
gloceries = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


def compute_bill(food):
    total=0
    for x in food:
        price= prices[x]
        if stock[x]>0:
           total=total +price
           stock[x]=stock[x] -1
    print(total)

compute_bill(gloceries)



