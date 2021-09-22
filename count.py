from collections import Counter

phones = ['Iphone', 'Samsung', 'LG', 'Iphone', 'LG']

count = Counter("Hello")
print(count)


text = "Мчался Эль Греко чрез бурную реку, лобстера там увидал...".lower().replace(' ','')
count = Counter(text)
print(count)
