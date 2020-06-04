def main():
    import random
    dice_sum = 0
    for i in range(0,2):
        roll = random.randint(1,6)
        dice_sum += roll
        print(f'You rolled {roll}')
    print(f'you have rolled total of {dice_sum}')    

if __name__== "__main__":
  main()
