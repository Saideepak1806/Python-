matrix=[
    [1,2,2],
    [2,2,3],
    [1,1,1]
]
target=3
found=False
for row in matrix:
    for val in row:
        if val==target:
            found=True
            break
if found:
    print("Target found")
else:
    print("Target not found")