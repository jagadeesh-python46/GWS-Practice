# ls = ['a','b','c','c','c','a','d']
# # print(ls.count('a'))
# ls1 = []
# count = 0
# for item in ls:
#   if item not in ls1:
#     count = 0
#     ls1.append(count)
#     ls1.append(item)
# else:
#    count += 1
# print(ls1)
#     # count_name = str(count) +str(ls[item])
#     # ls1.append(count_name)

# ls = ['a','b','c','c','c','a','d']

# string = ""
# count = 0
# current_string =None
# ls1 =[]

# for item in ls:
#     if item == current_string:
#         count = count+1
#     else:
        
ls = ['a','b','c','c','c','a','d']

disc = {}
print('type:', type(disc))

for item in ls:
    if item in disc: 
       disc[item] =  disc[item]+1
    else:
      disc[item] = 1
print(disc)

order =[]

for item in ls:
    if item not in order:
        order.append(item)
result = "".join(f"{disc[item]}{item}"
                  for item in order
                  )
print(result)
