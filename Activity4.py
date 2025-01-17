c1 = input("Enter the name of column:")
c2 = input("Enter the name of column:")
c3 = input("Enter the name of column:")

data_c1 = []
data_c2 = []
data_c3 = []

while True:
    print(f"\n Enter the data for:")
    data1 = input(f"{c1}")
    data2 = input(f"{c2}")
    data3 = input(f"{c3}")
    data_c1.append(data1)
    data_c2.append(data2)
    data_c3.append(data3)

    another = input("Do you want to continue? (y/n)")
    if another == "n":
        break

print("\n Formatted table")
print(f"{c1}                       {c2}                      {c3}")
print('-'*60)
for i in range (len(data_c1)):
    print(f"{data_c1[i]:<20} {data_c2[i]:<20} {data_c3[i]:<20}")