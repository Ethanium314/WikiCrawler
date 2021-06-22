import wikipedia as w
import threading

name = "python_(programming_language)"

dict = {}

def searchPage(page_name, dict, levels):
	if (levels == 0): return
	try: links = w.page(page_name).links
	except: return
	threads = []
	for link in links:
		if link in dict:
			dict[link] = 1
		else:
			dict[link] = 1
		x = threading.Thread(target=searchPage, args=(link, dict, levels - 1))
		threads.append(x)
		x.start()
		x.join()

searchPage(name, dict, 2)

print(dict)
