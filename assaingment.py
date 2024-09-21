# print how many - grocery products are available?


# "using for loop"
# # l=[]
# # for i in product_data['products']:
# #     if i['category']=='beauty':
# #         l.append(i)
# # print(l)
# "using filter and function"

# # def get_data(pr):
# #     return  pr['category']=='beauty'
# # a=list(filter(get_data,product_data['products']))
# # print(a)
# "using filter and lambada"
# # c=list(filter(lambda x:x['category']=='beauty',product_data['products']))
# # print(c)
# "using list comprehension"
# # print([i['category'] for i in product_data['products'] if i['category']=='beauty'])

# "using for loop"
# l=[]
# for i in product_data['products']:
#     if i['price']>2000:
#         l.append(i)
# print(l)
# "using filter and function"

# def get_data(pr):
#     return  pr['price']>2000
# a=list(filter(get_data,product_data['products']))
# print(a)
# "using filter and lambada"
# c=list(filter(lambda x:x['price']>2000,product_data['products']))
# print(c)
# "using list comprehension"
# print([i['price'] for i in product_data['products'] if i['price']>2000])