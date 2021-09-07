# count words given from user

passage = input("Floor is yours, write what's on your mind:\n")

words = passage.split(" ")
sentences = passage.split(".")

print(f"Thank you!\nYour passage has {len(sentences)} sentences and {len(words)} words.")
print(words)