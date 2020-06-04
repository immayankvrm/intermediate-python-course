def main():
    import random
    dice_sum = 0
    dice_size = int(input('how many sides are the dice'))
    dice_roll = int(input('size of the dice'))
    for i in range(0,dice_roll):
        roll = random.randint(1,6)
        dice_sum += roll
        if roll == 1:
            print(f'You rolled {roll}' 'critical fail')
        elif roll == dice_size :
            print(f'You rolled {roll}' 'critical success')

        else:
            (f'you rolled {roll}')

    print(f'you have rolled total of {dice_sum}')

if __name__== "__main__":
  main()
