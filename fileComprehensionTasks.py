# #task1
# numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
# newlist = [n for n in numbers if n > 0]
# print(newlist)
#
#
# #task2
# sentence = "The python is a general-purpose programming language, which uses the interpreter for translation"
# words = sentence.split(" ")
# result = [str(len(w)) for w in words if 'the' not in w]
# print(result)
#
# #task3
# div7 = [n for n in range(1,1000) if n % 7 == 0]
# print(div7)
#
#
# #task4
# three = [n for n in range(0,1000) if '3' in str(n)]
# print(three)
#
# #task5
# sentence = 'the slow solid squid swam sumptuously through the slimy swamp'
# spaces = [s for s in sentence if s == ' ']
# print(len(spaces))
#
# #task6
# sentence = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
# result = [l for l in sentence if l not in 'a,e,i,o,u, " "']
# print(result)
#
# #task7
# list_a = [1, 2, 3, 4]
# list_b = [2, 3, 4, 5]
# common = [a for a in list_a if a in list_b]
# print(common)

#task8
# sentence = "The python is a general-purpose programming language, which uses the interpreter for translation"
# result = [r for r in sentence if r in 'a, e, i, o, u,' and " " not in r]
# print(result)


#task9
input = [524, 458, 122, 455, 967]
output = [max([int(d) for d in n_str]) for n_str in [str(n) for n in input]]

print(output)