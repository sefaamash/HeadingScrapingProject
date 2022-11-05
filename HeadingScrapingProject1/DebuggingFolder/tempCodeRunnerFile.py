	h3s=bodyTag.find_all('h3')
	h2s=bodyTag.find_all('h2')
	h1s=bodyTag.find_all('h1')

	for h3 in h3s:
		
		print(h3.text)
	print("-----------------------------")
	for h2 in h2s:
		print(h2.text)
	print("-----------------------------")
	for h1 in h1s:
		print(h1.text)
	print("-----------------------------")
