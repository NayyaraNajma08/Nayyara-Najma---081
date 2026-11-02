guest_list = ["Vela", "Salsa", "Luna", "Shinta"]
print("unfortunately, the new table will not arrive on time")
print("I can only invite two guests for dinner.")

#remove guests untill only two remain
while len(guest_list) > 2:
    removed_guest = guest_list .pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner.")

#send invitation messages to the remaining guests
print("\nInvitation messages to the remaining guests:")
for guest in guest_list:
    print(f"Hello {guest}, you are still invited to dinner at my place.")
    
#delete the remaining guests
del guest_list[0]
del guest_list[0]


print(guest_list)