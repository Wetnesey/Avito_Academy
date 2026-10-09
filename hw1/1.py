def f(moscow: set, kazan: set):
	return moscow | kazan, moscow - kazan, kazan - moscow, moscow & kazan

moscow = {201, 202, 203, 204}
kazan = {203, 204, 205, 206}
print(f(moscow, kazan))