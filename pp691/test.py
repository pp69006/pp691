class test1:
	"""coucou c'est le deuxième test"""

	def fonc1(k):
		if k>0:
			print('oui')
		else:
			print('non')

	data = 1234
	

class tamere:

	def ta(suce):

		print(suce)

	def fille(pisse):
		return coucou

	
	
class VASIA:
	def derogatory_race_word(race = 'native_americans'):
   	 	"""
		Look for derogatory words about a specific race. We created it in order to create a list of native americans derogatory words but it can be applied to all the races available on: http://www.rsdb.org/races.
		The words come from this website : http://www.rsdb.org/

		Return the list of the derogatory words.

		Variables : "race" = should be taken from the list bellow. With default : 'native_americans'

		list of races on: http://www.rsdb.org/races
		"""


		from bs4 import BeautifulSoup
		import requests
		import re

		link = 'http://www.rsdb.org/race/' + race
		page_response = requests.get(link, timeout=5)
		page_content = BeautifulSoup(page_response.content, "html.parser")

		noresults = page_content.find('div', id="generic_message")
		if noresults != None:
		raise Exception('Wrong race name. If you need help to find race available for the function please check the website : http://www.rsdb.org/races')    

		x = page_content.find_all('a',href = re.compile('/slur'))
		derogatory = []

		for i in range(len(x)):
		derogatory.append(x[i].text)

		return derogatory
