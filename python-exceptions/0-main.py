#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list

# 1. Normal case
safe_print_list([1, 2, 3, 4], 2)

# 2. x == 0
safe_print_list([1, 2, 3], 0)

# 3. x > len(list)
safe_print_list([1, 2], 5)

# 4. x < 0 (negative index / invalid target)
safe_print_list([1, 2, 3], -1)

# 5. Empty list
safe_print_list([], 3)

# 6. List contains non-integers
safe_print_list(['a', 'b', 'c'], 'b')

# 7. List is None
safe_print_list(None, 2)

# 8. x is a string
safe_print_list([1, 2, 3], "2")

# 9. x is None
safe_print_list([1, 2, 3], None)

# 10. x is a float
safe_print_list([1, 2, 3], 2.0)

# 12. Nested list elements
safe_print_list([[1], [2], [3]], [2])

# 13. List contains `None`
safe_print_list([None, 1, 2], None)

# 14. x not in list
safe_print_list([10, 20, 30], 99)

