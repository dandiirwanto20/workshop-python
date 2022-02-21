def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# -- Do you have any Limburger ? (Output)
# -- I'm sorry, we're all out of Limburger (Output)
# It's very runny, sir. (Output)
# It's really very, VERY runny, sir. (Output)
# ---------------------------------------- (Output)
# shopkeeper : Michael Palin (Output)
# client : John Cleese (Output)
# sketch : Cheese Shop Sketch (Output)