def vowels_sentence(sentence:str) -> int:
    count = 0
    for char in sentence:
        if char in "aeiouAEIOU":
            count += 1
    return count    

print(vowels_sentence("Hello World"))