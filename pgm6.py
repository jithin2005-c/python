name_inp=input("Enter a list of names separated by spaces :")
names=name_inp.split()
count_a="".join(names).lower().count('a')
print("total occurrence of 'a':",count_a)
