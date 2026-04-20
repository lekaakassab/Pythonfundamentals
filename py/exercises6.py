#1
wordlist = ["apple", "banana", "apple"]
data = {}
for word in wordlist:
    if word in data:
        data[word] += 1
    else:
        data[word] = 1

for key in data:
    print(key, data[key])





#2
text = "apple,durian,banana,durian,apple,cherry,cherry,mango,apple,apple,cherry,durian,banana,apple,apple,apple,apple,banana,apple"
words = text.split(",")

data = {}

for word in words:
    if word in data:
        data[word] += 1
    else:
        data[word] = 1

for key in data:
    print(key, data[key])




#3
english_dutch = { "last":"laatst", "week":"week", "the":"de",
"royal":"koninklijk", "festival":"feest", "hall":"hal", "saw":
"zaag", "first":"eerst", "performance":"optreden", "of":"van",
"a":"een", "new":"nieuw", "symphony":"symphonie", "by":"bij",
"one":"een", "world":"wereld", "leading":"leidend", "modern":
"modern", "composer":"componist", "composers":"componisten",
"two":"twee", "shed":"schuur", "sheds":"schuren" }

sentence = "Last week The Royal Festival Hall saw the first \
performance of a new symphony by one of the world's leading \
modern composers, Arthur \"Two-Sheds\" Jackson."

words = sentence.lower().split()

for word in words:
    print(english_dutch.get(word, word))


#Split loop translate using dictionary


