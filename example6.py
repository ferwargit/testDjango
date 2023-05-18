# Remove elements from a Python List

shopping_list = ["Milk", "Pasta", "eggs", "spam", "bread", "rice"]
# Clear() method removes all elements from the list.
shopping_list.clear()
print(shopping_list)

shopping_list2 = ["Milk", "Pasta", "eggs", "spam", "bread", "rice"]
# pop() method removes the last item from the list.
shopping_list2.pop(1)
print(shopping_list2)

shopping_list3 = ["Milk", "Pasta", "eggs", "spam", "bread", "rice"]
# remove() method removes the specified item from the list.
shopping_list3.remove("eggs")
print(shopping_list3)