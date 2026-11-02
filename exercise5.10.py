usernames = ['vela', 'salsa', 'luna', 'admin', 'shinta']
new_usernames = ['vela', 'zeva', 'salma', 'uli', 'nadhira']

usernames_lower = [username.lower() for username in usernames]
for new_username in new_usernames:
    if new_username in usernames_lower:
        print(f"Username '{new_username}' is already taken.")
    else:
        print(f"Username '{new_username}' is available.")