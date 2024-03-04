import random

# Lists of first and last names
first_names = ["Bodatious", "Busty", "Beautiful", "Great", "Exeptional", "Sir","Mrs.","Mr.","Frisky","Fine","Glowing","Disabled","Radiant","Unliving","Spirit","Holy","The Grand"]
last_names = ["Moonchild","Skychild","Moonangel","Skyhawk","Runswater","Jahlomite","Jaahsslutte","Bloomingflower","Skyborn","MoonFather","Moonmother", "Moonpartner", "Servent"]

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
