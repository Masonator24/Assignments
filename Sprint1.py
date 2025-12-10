#These are the values of the coins
value = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}
#Sentence will be put in here
sentence_input = "sentence will go here"
#This will split input into parts that use "and"
pieces = sentence_input.split("and")
total = 0.0

for piece in pieces:
    #This will remove extra spaces and split the word into quantity(1st word/number), denomination(2nd word)
    piece = piece.strip()
    word = piece.split()
    quantity = int(word[0])
    coins = word[1]
    #Total is then added on by multiplying quantity by value
    total += quantity * value[coins]
print(round(total, 2))
