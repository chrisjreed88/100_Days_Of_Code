with open("file1.txt") as f1:
    file1_nums = f1.readlines()
    with open("file2.txt") as f2:
        result = [int(num) for num in f2 if num in file1_nums]

# Write your code above 👆

print(result)
