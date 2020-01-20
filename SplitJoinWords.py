def split_and_join(words):
    return "".join(words.split())


words = input("Enter the words here: ")
result = split_and_join(words)
print(result)
