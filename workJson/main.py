import json
from random import choice


def gen_person():
	name = ''
	tel = ''

	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
	nums = ['1', '2', '3', '4', '5', '6', '7']

	while len(name) != 5:
		name = name + choice(letters) # name += name + ...

	while len(tel) != 7:
		tel += choice(nums)

	person = {
		'name': name,
		'tel': tel
	}

	return person


def wr_js(person_dict):
	try:
		data = json.load(open('persons.json'))
	except:
		data = []

	data.append(person_dict)

	with open('persons.json', 'w') as file:
		json.dump(data, file, indent=2, ensure_ascii=False)


def main():

	for i in range(5):
		wr_js(gen_person()) #добавляем в список persons





if __name__ == '__main__':
	main()