import random

words=['vishal','python','machine']
sc=0
def shuf(word):
    word_char=list[word]
    random.shuffle(word_char)
    return ''.join(word_char)
def game():
    global sc
    if not words:
        print("all words guess")
        return False
    word=random.choice(words)
    words.remove(word)
    sh=shuf(word)
    print('\n guess the word',sh )
    at=3
    while at>0:
        guess=input(f' atttempts{4-at}/3 : enter the word : ').strip().lower()
        if guess==word:
            print("correct answere")
            sc+=3
            return True
        else:
            at-=1
            print("wrong word  try again")
        print(f"out of attempts ! the correct wpord is {word}")
        sc-=1
        return True
while game():
    print(f'your correct score : {sc}')

    

        

    