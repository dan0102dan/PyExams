# Пётр составляет таблицу кодовых слов для передачи сообщений, каждому сообщению соответствует своё кодовое слово. В качестве кодовых слов Пётр использует все пятибуквенные слова в алфавите {A, B, C, D, E, F}, удовлетворяющие такому условию: кодовое слово не может начинаться с буквы F и заканчиваться буквой A. Сколько различных кодовых слов может использовать Пётр?

letters = 'ABCDEF'
words = []

for a in letters[:-1]:
	for b in letters:
		for c in letters:
			for d in letters:
				for e in letters[1:]:
					word = a+b+c+d+e
					words.append(word)
print(len(words))