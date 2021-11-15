import re
import json

##
#	Gestion du dictionnaire des bonjour
##
class dict_hello:
	dictionary = None
	hello = []
	
	def __init__(self, file:str="hello.json"):
		with open(file) as hello_file:
			self.dictionary = json.load(hello_file)
		for i in self.dictionary.values():
			for j in i:
				self.hello.append(j)

class hello:
	hello_dict = dict_hello()

	##
	#	Permet d'apprendre une variante de salutation dans la langue demander ou dans une langue a créer
	#	@param	slef
	#	@param	word:str | Mot à apprendre
	#	@param	language:str | Langue de $word
	#	@return	bool | True si l'apprentissage a reussis et False si ça a échoué
	##
	def learn(self, word:str, language:str):
		if language in self.hello_dict.dictionary.keys():

			return True
		else:
			print(f"\"{language}\" n'exite pas veuillez choisire une autre langue ou l'ajouter")
			return False

	##
	#	Dit si la phrase dans la string est une salutaion à partire du dictionnaire HELLO
	#	@param	self
	#	@param	message:str = string à annalyser
	#	@return	bool
	##
	def isSay(self, message:str):	
		isDetect = False

		for possibility in self.hello_dict.hello:
			if re.compile(r'\b({0})\b'.format(possibility), flags=re.IGNORECASE).search(message) != None:
				isDetect = True
				break
		
		return isDetect