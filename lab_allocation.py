def allocate_lab(x, y, z, n):
    remaining_capacity = [x - n, y - n, z - n]
    min=float('inf')
    ans=['L1','L2','L3']
    for i in range(len(remaining_capacity)):
        if remaining_capacity[i]>=0 and remaining_capacity[i]<min:
            min=remaining_capacity[i]
            res=ans[i]
    
    return res

x = int(input("Capacity of lab L1: "))
y = int(input("Capacity of lab L2: "))
z = int(input("Capacity of lab L3: "))
n = int(input("Number of students in the class: "))
allocated_lab = allocate_lab(x, y, z, n)
print(allocated_lab)
    