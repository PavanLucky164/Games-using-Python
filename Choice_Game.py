from numpy import random
random_nums=random.randint(100,size=(5))
print(random_nums)
print("Select one number from given five numbers")
def game(random_nums):
    selected_num=int(input())
    if selected_num in random_nums:
        computer_selected_num=random.choice(random_nums,size=(1))
        if computer_selected_num == selected_num:
            print("You Won")
        else:
            print("You Lost")
    else:
        print(random_nums)
        print("Please select the number from the given five numbers")
        game(random_nums)
game=game(random_nums)
