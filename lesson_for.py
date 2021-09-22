from lessons_if import discounted

stock = [
		{'name': 'iPhone 12', 'stock': 24, 'price': 65432.1, 'discount': 25},
		{'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000.0,'discount': 10},
		{'name': '', 'stock': 18, 'price': 10000.0, 'discount': 10}
]

for phone in stock:
    phone['final price'] = discounted(phone['price'], phone['discount'], name=phone['name'])
    print(stock)
