from random import choices

urballs = str(input('UrBalls : What is your question = '))
print('UrBalls : Your question is = ', urballs)

list_answer = [
    "It is decidedly so",
    "Without a doubt",
    "Yes definitely",
    "You may rely on it"
]

if __name__ == "__main__" :
    print('UrBalls :', choices(list_answer)[0])