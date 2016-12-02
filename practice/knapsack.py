'''
Imagine the following situations:

A truck loading cargo
A shopper on a budget
A thief stealing from a house using a large bag
A child eating candy very quickly
All of these are examples of The Knapsack Problem, where there are more things that you want to take with you than you can take with you.

The Problem

Given a container with a certain capacity and an assortment of discrete items with various sizes and values (and an infinite supply of each item), determine the combination of items that fits within the container and maximizes the value of the collection.

However, DO NOT attempt to solve the problem EXACTLY! (we will do that in Part 2)

The Simplification

Because the optimal collection of items is MUCH more difficult to determine than a nearly-optimal collection, this kata will only focus on one specific nearly-optimal solution: the greedy solution. The greedy solution is that which always adds an item to the collection if it has the highest value-to-size ratio.

For example, if a "greedy thief" with a 10-Liter knapsack sees two types of items

a 6-Liter item worth $9 (1.5 $/L)
a 5-Liter item worth $5 (1.0 $/L)
the thief will take 1 of the 6-Liter items instead of 2 of the 5-Liter items. Although this means the thief will only profit $9 instead of $10, the decision algorithm is much simpler. Maybe the thief is bad at math.

Now, go be bad at math!

The Kata

Write the function knapsack that takes two parameters, capacity and items, and returns a list of quantities.

capacity will be a positive number

items will be an array of arrays of positive numbers that gives the items' sizes and values in the form [[size 1, value 1], [size 2, value 2], ...]

knapsack will return an array of integers that specifies the quantity of each item to take according to the greedy solution (the order of the quantities must match the order of items)

Source: https://www.codewars.com/kata/53ffbba24e9e1408ee0008fd/train/python
'''

# solution
import numpy as np

def knapsack(capacity, items):
    # Be greedy!
    item_to_size = [value/float(size) for size, value in items]
    final = [0 for i in range(len(items))]
    for i in np.argsort(item_to_size)[::-1]:
        size, value = items[i]
        final[i] = int(capacity/size)
        capacity = capacity % size
    return final

# tests
Test.assert_equals(knapsack(100, ((1, 1),)), [100])
Test.assert_equals(knapsack(100, ((100, 1),)), [1])


Test.describe('Two items')
Test.assert_equals(knapsack(100, ((1, 1),
                                  (3, 4))), [1, 33])
Test.assert_equals(knapsack(100, ((60, 80),
                                  (50, 50))), [1, 0])


Test.describe('Three items')
Test.assert_equals(knapsack(100, ((10, 10),
                                  (30, 40),
                                  (56, 78))), [1, 1, 1])
Test.assert_equals(knapsack(100, ((11.2,  7.4),
                                  (25.6, 17.8),
                                  (51.0, 41.2),
                                  (23.9, 15.6),
                                  (27.8, 19.0))), [2, 1, 1, 0, 0])
