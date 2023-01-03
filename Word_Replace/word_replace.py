def wordreplace():
    sentence = "hello hello hello i am here to say hello!"
    print("Current sentence: " + sentence)
    word_replaced = input("Enter word to be replaced: ")
    word_replacing = input("Enter word replacement: ")
    return (sentence.replace(word_replaced, word_replacing))

print(wordreplace())
