def second_highest_vowel_occurrence(string):
    # Define vowels
    vowels = 'aeiou'

    # Initialize a dictionary to store the count of each vowel
    vowel_count = {x: 0 for x in vowels}


    # Count occurrences of each vowel in the string
    for char in string.lower():
        if char in vowel_count:
            vowel_count[char] += 1

    # Get a sorted list of counts in descending order
    sorted_counts = sorted(vowel_count.values(), reverse=True)

    # If there is no second-highest occurrence, return a message
    if len(sorted_counts) < 2 or sorted_counts[1] == 0:
        return "No second highest vowel occurrence"

    # Find the second highest occurrence
    second_highest = sorted_counts[1]

    return second_highest


# Example usage:
input_string = "fun"
result = second_highest_vowel_occurrence(input_string)
print("Second highest vowel occurrence:", result)





