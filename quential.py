import itertools

def generate_wordlist(input_string, min_length=None, max_length=None):
    # Remove whitespace characters from the input string
    input_string = ''.join(input_string.split())
    
    # Generate all permutations of the characters in the input string
    perms = [''.join(p) for p in itertools.permutations(input_string)]
    
    # Filter permutations based on minimum and maximum lengths if specified
    if min_length is not None and max_length is not None:
        perms = [p for p in perms if min_length <= len(p) <= max_length]
    
    return perms

if __name__ == "__main__":
    # Get input from the user
    input_string = input("Enter values. E.g. Alien 1900 or Jon Doe Art or Jane Hockey 20: ")

    # Ask the user if they want to specify minimum and maximum lengths for words
    if input("Do you want to specify minimum and maximum lengths? (y/n): ").lower() == "y":
        # Get minimum and maximum lengths from the user
        min_length_input = input("Enter the minimum length of the output words: ")
        max_length_input = input("Enter the maximum length of the output words: ")
        min_length = int(min_length_input)
        max_length = int(max_length_input)
    else:
        min_length = None
        max_length = None

    # Ask the user for a name for the generated wordlist
    wordlist_name = input("Enter a name for the generated wordlist (press Enter to use default): ")

    # Generate the wordlist
    wordlist = generate_wordlist(input_string, min_length, max_length)

    # If no name is provided, use a default name
    if not wordlist_name:
        wordlist_name = "gen_wordlist"

    # Write the wordlist to a text file
    with open(f"{wordlist_name}.txt", "w") as f:
        for word in wordlist:
            f.write(word + "\n")

    # Print a message indicating that the wordlist has been generated successfully
    print(f"Wordlist '{wordlist_name}.txt' has been generated successfully.")
