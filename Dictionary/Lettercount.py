#program to count the letter in string
def count_letter():
    string ="w3resource"
    print(string)
    all_freq = {}

    for i in string:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    print("the count of letter in string",str(all_freq))
count_letter()
