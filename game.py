from random import choice

(lambda n: print('Hello,', n))(name := input('Enter your name: '))
with open('rating.txt', 'r') as file:
    score = int([(0, line.split(' ')[1])[name == line.split(' ')[0]] for line in file][0])
options = (lambda i: (('rock', 'paper', 'scissors'), i.split(','))[bool(i)])(input())
print("Okay, let's start")
while (player := input()) != '!exit':
    if player not in options:
        print(('Invalid input', f'Your rating: {score}')[player == '!rating'])
        continue
    options = (lambda c: options[c:] + options[:c])(options.index(computer := choice(options)))
    result = ((-1, 1)[options.index(player) <= (len(options) // 2)], 0)[computer == player]
    print((f'There is a draw ({player})', f'Well done. The computer chose {computer} and failed',
           f'Sorry, but the computer chose {computer}')[result])
    score += (50, 100, 0)[result]
print('Bye!')
