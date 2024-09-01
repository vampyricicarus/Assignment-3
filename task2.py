# task 1

attendees = input("Enter number of attendees: ")
venue = "large hall" if int(attendees) > 100 else "conference room"
print(venue)
equipment = "audio system" if int(attendees) > 100 else "projector"
print(equipment)
# i corrected the integer to string issue in the code
# then i added the variable for equipment to use

foodPreference = input("Are you vegetarian? ")
foodServed = "Veggie Delight Caterers" if foodPreference == "yes" else "Gourmet Meals Caterers"
# using shorthand to add meal options