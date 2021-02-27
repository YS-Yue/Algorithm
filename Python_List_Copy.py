import copy


def main():

    print("1. Try '='\n")

    old_1 = [1, 2, 3, 4]
    new_1 = old_1
    print_old_vs_new(old_1, new_1)
    # Old List is : [1, 2, 3, 4]
    # New List is :[1, 2, 3, 4]
    print(id(old_1))
    print(id(new_1))
    # 140420109309984
    # 140420109309984

    print("\nModify new list:\n")

    new_1.append(5)
    print_old_vs_new(old_1, new_1)
    # Old List is : [1, 2, 3, 4, 5]
    # New List is :[1, 2, 3, 4, 5]

    print("\nModify old list:\n")
    old_1.pop()
    print_old_vs_new(old_1, new_1)
    # Old List is : [1, 2, 3, 4]
    # New List is :[1, 2, 3, 4]
    
    print("\n2. Try slice[:]\n")
    old_2 = [1, 2, 3, 4]
    new_2 = old_2[:]
    print_old_vs_new(old_2, new_2)
    # Old List is : [1, 2, 3, 4]
    # New List is :[1, 2, 3, 4]
    print(id(old_2))
    print(id(new_2))
    # 140420106163776
    # 140420109433984 

    print("\nModify new list:\n")

    new_2.insert(0, -1)
    print_old_vs_new(old_2, new_2)
    # Old List is : [1, 2, 3, 4]
    # New List is :[-1, 1, 2, 3, 4]

    print("\nModify old list:\n")   
    old_2.pop()
    print_old_vs_new(old_2, new_2)
    # Old List is : [1, 2, 3]
    # New List is :[-1, 1, 2, 3, 4]

    print("\n3. Try .copy()\n")
    old_3 = [1, 2, 3, 4]
    new_3 = old_3.copy()
    print_old_vs_new(old_3, new_3)
    # Old List is : [1, 2, 3, 4]
    # New List is :[1, 2, 3, 4]
    print(id(old_3))
    print(id(new_3))
    # 140420109433904
    # 140420111736096

    print("\nModify new list:\n")

    new_3[0] = "x"
    print_old_vs_new(old_3, new_3)
    # Old List is : [1, 2, 3, 4]
    # New List is :[-1, 1, 2, 3, 4]
    
    print("\nModify old list:\n")   
    old_3[-1] = "z"
    print_old_vs_new(old_3, new_3)
    # Old List is : [1, 2, 3, 4]
    # New List is :[1, 2, 3, 4]


    print("\n4. Try copy.deepCopy()\n")
    old_4 = [1, 2, 3, 4]
    new_4 = copy.deepcopy(old_4)
    print_old_vs_new(old_4, new_4)
    # Old List is : [1, 2, 3, 4]
    # New List is :[1, 2, 3, 4]
    print(id(old_4))
    print(id(new_4))  
    # 140420111736736
    # 140420111736256

    print("\nModify new list:\n")

    new_4[0] = "x"
    print_old_vs_new(old_4, new_4)
    # Old List is : [1, 2, 3, 4]
    # New List is :[-1, 1, 2, 3, 4]
    
    print("\nModify old list:\n")   
    old_4[-1] = "z"
    print_old_vs_new(old_4, new_4)
    # Old List is : [1, 2, 3, 4]
    # New List is :[1, 2, 3, 4]


def print_old_vs_new(oldList, newList):
    print("Old List is : ", end="")
    print(oldList)
    print('New List is :', end="")
    print(newList)


main()
