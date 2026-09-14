text = "Welcome to Python! Programming is fun and easy to learn."

char_count = len(text)
word_count = len(text.split())
sentence_count = text.count(".") + text.count("!") + text.count("?")

if sentence_count == 0 and word_count > 0:
    sentence_count = 1

print("Original Text:", text)
print("Characters:", char_count)
print("Words:", word_count)
print("Sentences:", sentence_count)