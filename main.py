
buying_of_prod = {
    "piekarni": ["chleb", "bułki", "pączki"],
    "warzywniaka": ["marchew", "seler", "rukola"]
}
print("Lista zakupów", "\n")
for shop in buying_of_prod:
    print(f"Idę do {shop.capitalize()}", "i kupuję tam:", (buying_of_prod[shop]))
print("W sumie kupuję:", len(buying_of_prod["piekarni"]) + len(buying_of_prod ["warzywniaka"]), "produktów")
