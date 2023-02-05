
buying_of_prod = {
    "piekarni": ["chleb", "bułki", "pączki"],
    "warzywniaka": ["marchew", "seler", "rukola"]
}
print("Lista zakupów", "\n")

for shop in buying_of_prod:
    print(f"Idę do {shop.capitalize()}", "i kupuję tam:", (buying_of_prod[shop]))
   
all_products = 0
for values in buying_of_prod.values():
    all_products += len(values)
print("W sumie kupuję:{} produktów".format(all_products))
