import pymongo


# Config MongoDB


uri = "mongodb://admin:admin@ds119598.mlab.com:19598/cafeteria"


client = pymongo.MongoClient(uri)


db = client.get_default_database()

# Get MENU collection


menu_items = db["menu"].find()


menu_items_length = db["menu"].count()

# Get ORDER collection

order_items = db["order"].find()


order_items_length = db["order"].count()

#Turn 9
for i in range(order_items_length):
    order_value_length = len(order_items[i]["order"])
    total_money1 = 0
    for k in range(order_value_length):        
        for n in range(menu_items_length ):
            if menu_items[n]["name"] == order_items[i]["order"][k]:
                price_of_food = menu_items[n]["price"]
        total_money1 += price_of_food   
    print(total_money1)
