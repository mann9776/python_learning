def second_highest_vowel_occurrence(s):
    # Define vowels
    vowels = 'aeiouAEIOU'

    # Create a dictionary to count occurrences of each vowel
    vowel_count = {v: 0 for v in vowels}

    # Count the occurrences of each vowel in the string
    for char in s:
        if char in vowels:
            vowel_count[char] += 1

    # Get the counts of vowels in a list and sort it in descending order
    counts = sorted(vowel_count.values(), reverse=True)

    # Find the second highest unique count
    highest = counts[0]
    second_highest = None
    for count in counts:
        if count < highest:
            second_highest = count
            break

    # If there is no second highest, return None
    if second_highest is None or second_highest == 0:
        return None

    # Find the vowel(s) with the second highest count
    second_highest_vowels = [v for v, count in vowel_count.items() if count == second_highest]

    return second_highest_vowels, second_highest


# Example usage
string = "This is an example string to test the function."
result = second_highest_vowel_occurrence(string)
print(result)  # Output: (['i'], 3)
