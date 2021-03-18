# words = ['мадам', 'топот', 'test', 'madam', 'word']
# l1 = [i for i in words if i == i[::-1]]
# print (l1)
my_str = ['Око за око','А роза упала на лапу Азора','Около Миши молоко']
l1 = []
for word in my_str:
    word_r = word.replace(' ', '').lower()
    if word_r == word_r[::-1]:
        l1.append(word)
print(l1)
