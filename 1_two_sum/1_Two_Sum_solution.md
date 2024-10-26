# 1. Two Sum - Solution


## Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
I was thinking about data types and their methods which have O(n) time complexities. The most obvious option to me is using dictionary as its `.get()` method takes O(1) time.

## Approach
<!-- Describe your approach to solving the problem. -->
1) Create a for loop with `range()` function which takes O(1) run time.
2) Inside this loop:
    2.1) retive a list item and calculate the second addend to get the target value
    2.2) Check if the second addend is in dictionary keys. If it is:
        2.2.1) return an array with the value of the index of this key was calculated and the current index from the range in the loop.

## Complexity
### - Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
__O(n).__
The solution iterates through the list once, creating a dictionary with each entry (`num_dict[item] = i`) and checking for `second_addend` in the dictionary (both O(1) operations). This makes the loop itself O(n) in time complexity.

### - Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
__O(n).__
The dictionary `num_dict` stores each element in `nums` as it iterates, so in the worst case, it holds n entries, making space complexity O(n).
