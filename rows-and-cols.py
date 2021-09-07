# Put and X into a grid

row1 = ["~", "~", "~"]
row2 = ["~", "~", "~"]
row3 = ["~", "~", "~"]

# now create a grid/map
grid = [row1, row2, row3]
# print it out
print(f"{row1}\n{row2}\n{row3}")

# prompt user
mark = input("This is a 3 x 3 grid. Place your coordinates(row first then column: ")
grid[int(mark[0]) - 1][int(mark[1]) - 1] = "X"  # avoid IndexOutOfBound error - otherwise user must enter num (0-2) instead of (1-3)

print(f"{row1}\n{row2}\n{row3}")

