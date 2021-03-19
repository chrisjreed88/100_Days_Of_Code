row1 = ["#", "#", "#"]
row2 = ["#", "#", "#"]
row3 = ["#", "#", "#"]
map = [row1, row2, row3]
print("Here's the treasure map\n")
print("  1    2    3")
print(f"1{row1}\n2{row2}\n3{row3}\n")
position = input("Where do you want to put the treasure?\n")
row = int(position[0]) - 1
column = int(position[1]) - 1

map[row][column] = "X"
print(f"1{row1}\n2{row2}\n3{row3}\n")
