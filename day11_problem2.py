nums = [1, 2, 3, 4, 5, 6, 7, 8]

fizz_list = ["fizz" if x % 3 == 0 else x for x in nums]
print(fizz_list)