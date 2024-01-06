"""
Nathan Gu and Blake Potvin
Sorting Project - Starter
CSE 331 Fall 2023
"""

import random
import time
from typing import TypeVar, List, Callable, Dict, Tuple
from dataclasses import dataclass

T = TypeVar("T")  # represents generic type


# do_comparison is an optional helper function but HIGHLY recommended!!!
def do_comparison(first: T, second: T, comparator: Callable[[T, T], bool], descending: bool) -> bool:
    """
    Returns True if first argument should come before second argument and False otherwise
    :param first: first value to compare, second: second value to compare, comparator: comparator function, descending: if list should be in descending order
    """
    if (comparator(first, second) and not descending) or (not comparator(first, second) and descending):
        return True
    else:
        return False


def selection_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                   descending: bool = False) -> None:
    """
    Sorts a list using insertion sort.
    :param data: Data to sort, comparator: comparator function, descending: if list should be in descending order
    """
    for i in range(len(data)):
        minIndex = 0
        minVal = data[i]
        for j in range(i+1, len(data)):
            if not do_comparison(minVal, data[j], comparator, descending):
                minIndex = j
                minVal = data[j]
        if minVal != data[i]:
            data[i], data[minIndex] = data[minIndex], data[i]



def bubble_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                descending: bool = False) -> None:
    """
    Sorts a list using bubble sort.
    :param data: Data to sort, comparator: comparator function, descending: if list should be in descending order
    """
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if not do_comparison(data[i], data[j], comparator, descending):
                data[i], data[j] = data[j], data[i]



def insertion_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                   descending: bool = False) -> None:
    """
    Sorts a list using insertion sort.
    :param data: Data to sort, comparator: comparator function, descending: if list should be in descending order
    """
    for index in range(1, len(data)):
        i = index
        j = i - 1
        while j >= 0 and do_comparison(data[i], data[j], comparator, descending):
            data[i], data[j] = data[j], data[i]
            j -= 1
            i -= 1




def hybrid_merge_sort(data: List[T], *, threshold: int = 12,
                      comparator: Callable[[T, T], bool] = lambda x, y: x < y, descending: bool = False) -> None:
    """
    Sorts a list using merge sort on any array with length greater than the threshold argument and
    insertion sort otherwise.
    :param data: Data to sort, threshold: int argument, comparator: comparator function, descending: if list should be in descending order
    """

    def merge(left: List[T], right: List[T]):
        i, j, k = 0, 0, 0
        len1, len2 = len(left), len(right)
        while i < len1 and j < len2:
            if do_comparison(left[i], right[j], comparator, descending):
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1
        while i < len1:
            data[k] = left[i]
            i += 1
            k += 1
        while j < len2:
            data[k] = right[j]
            j += 1
            k += 1

    if len(data) <= threshold:
        insertion_sort(data, comparator=comparator, descending=descending)
        return
    elif len(data) <= 1:
        return

    left, right = 0, len(data)
    mid = (left + right) // 2
    left_data = data[:mid]
    right_data = data[mid:]
    hybrid_merge_sort(left_data, threshold=threshold, comparator=comparator, descending=descending)
    hybrid_merge_sort(right_data, threshold=threshold, comparator=comparator, descending=descending)
    merge(left_data, right_data)



def maximize_rewards(item_prices: List[int]) -> (List[Tuple[int, int]], int):
    """
    Maximize possible rewards for a Conrad's order
    :param item_prices: list of item prices to maximize rewards for
    """
    tup = ([],-1)
    if not item_prices:
        return tup
    if len(item_prices) % 2 == 1:
        return tup
    res = []
    points = 0
    hybrid_merge_sort(item_prices)
    l, r = 0, len(item_prices) - 1
    target = item_prices[0] + item_prices[len(item_prices) - 1]
    while l < r:
        if target != item_prices[l] + item_prices[r]:
            return tup
        else:
            newTup = (item_prices[l], item_prices[r])
            res.append(newTup)
            points += item_prices[l] * item_prices[r]
        l += 1
        r -= 1
    return (res, points)



def quicksort(data) -> None:
    """
    Sorts a list in place using quicksort
    :param data: Data to sort
    """

    def quicksort_inner(first, last) -> None:
        """
        Sorts portion of list at indices in interval [first, last] using quicksort

        :param first: first index of portion of data to sort
        :param last: last index of portion of data to sort
        """
        # List must already be sorted in this case
        if first >= last:
            return

        left = first
        right = last

        # Need to start by getting median of 3 to use for pivot
        # We can do this by sorting the first, middle, and last elements
        midpoint = (right - left) // 2 + left
        if data[left] > data[right]:
            data[left], data[right] = data[right], data[left]
        if data[left] > data[midpoint]:
            data[left], data[midpoint] = data[midpoint], data[left]
        if data[midpoint] > data[right]:
            data[midpoint], data[right] = data[right], data[midpoint]
        # data[midpoint] now contains the median of first, last, and middle elements
        pivot = data[midpoint]
        # First and last elements are already on right side of pivot since they are sorted
        left += 1
        right -= 1

        # Move pointers until they cross
        while left <= right:
            # Move left and right pointers until they cross or reach values which could be swapped
            # Anything < pivot must move to left side, anything > pivot must move to right side
            #
            # Not allowing one pointer to stop moving when it reached the pivot (data[left/right] == pivot)
            # could cause one pointer to move all the way to one side in the pathological case of the pivot being
            # the min or max element, leading to infinitely calling the inner function on the same indices without
            # ever swapping
            while left <= right and data[left] < pivot:
                left += 1
            while left <= right and data[right] > pivot:
                right -= 1

            # Swap, but only if pointers haven't crossed
            if left <= right:
                data[left], data[right] = data[right], data[left]
                left += 1
                right -= 1

        quicksort_inner(first, left - 1)
        quicksort_inner(left, last)

    # Perform sort in the inner function
    quicksort_inner(0, len(data) - 1)
