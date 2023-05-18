shopping_list = ["Milk", "Pasta", "eggs", ["spam", "bread"]]
print(shopping_list[3])
['spam', 'bread']

print(shopping_list[3][1])
shopping_list[3][0] = "butter"
# bread

print(shopping_list)
# ['Milk', 'Pasta', 'eggs', ['butter', 'bread']]

shopping_list2 = ["Milk", "Pasta", "eggs", ["spam", "bread"]]
shopping_list2.insert(0, "New")
print(shopping_list2)
# ['New', 'Milk', 'Pasta', 'eggs', ['spam', 'bread']]

shopping_list3 = ["Milk", "Pasta", "eggs", ["spam", "bread"]]
shopping_list3[3].insert(0, "butter")
print(shopping_list3)
# ['Milk', 'Pasta', 'eggs', ['butter', 'spam', 'bread']]

shopping_list4 = ["Milk", "Pasta", "eggs", ["spam", "bread"]]
shopping_list4[3].extend("New")
print(shopping_list4)
# ['Milk', 'Pasta', 'eggs', ['spam', 'bread', 'N', 'e', 'w']]

shopping_list5 = ["Milk", "Pasta", "eggs", ["spam", "bread"]]
# shopping_list5[3].extend(("New",))
shopping_list5[3].extend(["New"])
print(shopping_list5)
# ['Milk', 'Pasta', 'eggs', ['spam', 'bread', 'New']]

shopping_list6 = ["Milk", "Pasta", "eggs", ["spam", "bread",["Pan", "Leche"]]]
print(shopping_list6[3][2][1])
# 'Leche'