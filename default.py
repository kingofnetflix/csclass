input = input("Do you like Nyan Cat? ").strip().lower()
if input in ["yes", "y", "yeah", "yep"]:
    print("Nyan Cat is awesome!")
elif input in ["no", "n", "nope"]:
    print("That's too bad.")
else:
    print("I don't understand that response.")

