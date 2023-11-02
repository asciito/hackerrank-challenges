import os
from collections import Counter

def counter(shoe_sizes: list, customers: list):
    earnings = 0

    for customer in customers:
        size, price = customer.split(' ')
        size, price = int(size), int(price)

        if shoe_sizes.get(size) is None or shoe_sizes.get(size) < 1:
            continue

        shoe_sizes.subtract([size])
        earnings += price

    return earnings


if __name__ == '__main__':
    root_dir = os.path.join(os.path.dirname(__file__), 'input')

    for root, _, files in os.walk(root_dir):    
        for file in files:
            with open(os.path.join(root, file), 'r') as f:
                input_values = f.readlines()
            
            shoe_sizes = Counter([int(x) for x in input_values[1].split(' ')])
            customers  = input_values[3:-1]
            result     = int(input_values[-1])

            ans = counter(shoe_sizes, customers)

            if ans != result:
                print(f'The answer is incorrect: answer({ans}) != result({result})')
            else:
                print(f'{file}: Raghu earn -> {ans}')