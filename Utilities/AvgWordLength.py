import string
x = "hello !!!world @@#"

def avgWordLength(sentence):

    print(f"Original sentence: {sentence}")

    #Remove punctuation
    sentence = sentence.translate(sentence.maketrans("","",string.punctuation))
    print(f"Step 1: Remove punctuation: {sentence}")

    lst=sentence.strip().split(" ")
    print(f"Step 2: Turn string to list: {lst}")

    #use map in order to calculate the length for each string
    lst_len = list(map(len,lst))
    print(f"Step 3: Length list: {lst_len}")

    #Calculate the average word length and return the value
    print(f"sum: {sum(lst_len)}, length: {len(lst_len)}")
    return sum(lst_len)/len(lst_len)


print(avgWordLength(x))