
# coding: utf-8

# In[ ]:

'''This script demonstrates simulations of coin flipping'''
import random
import matplotlib.pyplot as plt

# let's create a fair coin object that can be flipped:

class Coin(object):
    '''this is a simple fair coin, can be pseudorandomly flipped'''
    sides = ('heads', 'tails')
    last_result = None

    def flip(self):
        '''call coin.flip() to flip the coin and record it as the last result'''
        self.last_result = result = random.choice(self.sides)
        return result

# let's create some auxilliary functions to manipulate the coins:

def create_coins(number):
    '''create a list of a number of coin objects'''
    return [Coin() for _ in xrange(number)]

def flip_coins(coins):
    '''side effect function, modifies object in place, returns None'''
    for coin in coins:
        coin.flip()

def count_heads(flipped_coins):
    return sum(coin.last_result == 'heads' for coin in flipped_coins)

def count_tails(flipped_coins):
    return sum(coin.last_result == 'tails' for coin in flipped_coins)

def main():
    coins = create_coins(1000)
    head_count = []
    max_count = []
    min_count = []
    for i in xrange(100):
        flip_coins(coins)
        head_count.append(count_heads(coins))
        
        if count_heads(coins) < count_tails(coins):
            max_count.append(count_tails(coins))
            min_count.append(count_heads(coins))
        else:
            max_count.append(count_heads(coins))
            min_count.append(count_tails(coins))
           
    plt.figure()
    plt.hist(head_count, 10)
    plt.xlabel('Number of Heads')
    plt.ylabel('Frequency')
    plt.title('Number of Heads in 1000 Coins')
    plt.show()
    
    plt.figure()
    plt.hist(max_count, 10, facecolor = 'green', alpha = 0.50)
    plt.hist(min_count, 10, facecolor = 'blue', alpha = 0.50)
    plt.xlabel('Coin Count')
    plt.ylabel('Frequency')
    plt.title('Min and Max Counts')
    plt.legend(['Max Count', 'Min Count'])
    plt.show()

if __name__ == '__main__':
    main()


# In[2]:

#The number of heads from flipping 1000 coins was tracked for 100 trails.
#The distribution for the number of heads resembles a normal (Gaussian)
#distribution which is expected.  The number of heads in a particular
#trial is not binary although flipping a coin has a binary
#outcome (heads or tails).  Some trials will have more heads and others
#will have fewer heads which is caused by the randomness of flipping
#a fair coin.  

#The distribution for min and max follows a half-width normal (Gaussian)
#distrubtion.

