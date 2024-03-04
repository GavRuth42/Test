import random

# Lists of first and last names
first_names = ["Chucklefuck", "Dogtail", "MeatPants", "Bitchboy", "Shitbag", "Cleetus","Fuckface","Todd Howard","Kevin" ]
last_names = ["Mckrinkleberry", "Biggums", "Dingleberry", "Jones", "McBrownpants", "Wankenshire","the 25th","Of Mogadishu"]

def generate_random_name():
    """Generate a random name."""
    random_first_name = random.choice(first_names)
    random_last_name = random.choice(last_names)
    return f"{random_first_name} {random_last_name}"

def main():
    """Main function to generate and print random names."""
    for _ in range(1):  # Generate and print 1 random name
        random_name = generate_random_name()
        print(random_name)

if __name__ == "__main__":
    main()
