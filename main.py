

song = "I like to eat, eat, eat, apples and bananas"



# def sing(vowel):
#     new_scentence = ""
#     for charachter in song:
#       new_scentence = new_scentence * 3
#     print(new_scentence)



# sing("ay")
# sing("ee")
# sing("i")
# sing("o")
# sing("u")


song = "I like to eat, eat, eat, apples and bananas"

def sing(vowel):
    print(song[:20].replace("a", vowel)+ song[20:])
    


sing("ay")
sing("ee")
sing("i")
sing("o")
sing("u")