g = ["Geeky", "GeeksforGeeks", "SuperGeek", "Geek"]
ind = [0, 1, "2", 3]
for i in range(len(ind)):
	try:
		print(g[ind[i]])
	except TypeError:
		print("TypeError: Check list of indices")
