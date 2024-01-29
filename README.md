# Sorting Project README
## Overview
This project for CSE 331 Fall 2023, focuses on implementing various sorting algorithms in Python. The project showcases how different sorting techniques can be implemented and used effectively in different scenarios.

## Features
Selection Sort: A simple comparison-based sorting algorithm.<br />
Bubble Sort: A popular sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.<br />
Insertion Sort: Builds a sorted array (or list) one element at a time by comparing and inserting elements into their correct position.<br />
Hybrid Merge Sort: A combination of merge sort and insertion sort, utilizing the best aspects of both algorithms depending on the size of the data subset.<br />
Maximize Rewards: A specific function designed to maximize rewards based on item prices, demonstrating a practical application of sorting algorithms.<br />
Quicksort: An efficient, in-place sorting algorithm, which is a comparison sort, meaning that it can sort items of any type for which a "less-than" relation is defined.<br />
Usage
Sorting Data: To sort data using any of these algorithms, simply pass your data list to the corresponding function along with an optional comparator function and a boolean indicating the sorting order.<br />
Maximizing Rewards: To maximize rewards, use the maximize_rewards function by passing a list of item prices.<br />
Example
python<br />

from sorting_starter import selection_sort, maximize_rewards<br />

### Example of Selection Sort
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]<br />
selection_sort(data)<br />
print(data)<br />

### Example of Maximizing Rewards
item_prices = [10, 15, 10, 20, 15, 20]<br />
pairs, points = maximize_rewards(item_prices)<br />
print(pairs, points)<br />

## Installation<br />
No special installation is required apart from having Python 3.7 or above.

## Dependencies
Python 3.7+

## Author
Dallas Foley
