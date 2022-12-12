import random

def get_choices():
    options = ['rock', 'paper', 'scissors']
    player_choice = input('Enter a choice (rock, paper, scissors): ').lower()

    #Check statement
    while player_choice not in options:
        player_choice = input('Please only enter rock, paper or scissors: ').lower()

    computer_choice = random.choice(options)
    choices = {'player': player_choice, 'computer': computer_choice}
    return choices
    
def check_win(player, computer):
    print(f'You chose {player}, computer chose {computer}')
    if player == computer:
        return "It's a tie!"
    elif player == 'rock':
            if computer == 'scissors':
                return 'Rock smashes scissors! You win!'
            else:
                return 'Paper covers rock! You lose.'
    elif player == 'paper':
            if computer == 'rock':
                return 'Paper covers rock! You win!'
            else:
                return 'Scissors cuts paper! You lose.'            
    elif player == 'scissors':
            if computer == 'paper':
                return 'Scissors cuts paper! You win!'
            else:
                return 'Rock smashes scissors! You lose.'

choices = get_choices()
result = check_win(choices['player'], choices['computer'])
print(result)

#Example Calling functions
#def greeting():
#    return 'Hi'
#response = greeting()
#print(response)


#Example Dictionaries
#dict = {'name': 'beau', 'color': 'blue'}


#Exmaple List
#food = ['pizza', 'carrots', 'eggs']
#dinner = random.choice(food)


#Exmaple if, else, elif
#age = 20
#if age >= 18:
#    print('You are an adult.')
#elif age > 12:
#    print('You are a teenager.')
#elif age > 1:
#    print('You are a child.')
#else
#    print('You are a baby.')


#Example f string
#age = 25
#print(f'Jim is {age} year old.')


#Example Data Type and Casting
#name = 'something'
#print(type(name))
#print(isinstance(name, str))
#age = 2 #can make it float by float(2)
#print(isinstance(age, float)) #false since it's not a decimal number