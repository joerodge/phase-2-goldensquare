def get_most_common_letter(text):
    counter = {}
    for char in text:
        # Only count letters
        if char.isalpha():
            counter[char] = counter.get(char, 0) + 1

    # Need to reverse sort as normal sort starts at lowest number
    # but we need the highest
    sorted_letters = sorted(counter.items(), key=lambda item: item[1], reverse=True)
    
    # Need the first (index 0) pair as that will have highest count based on sort
    # and then the key in that pair which is at index 0 i.e. [0][0]
    return sorted_letters[0][0]


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")