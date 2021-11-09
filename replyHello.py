import re
import json

##
 # Gestion du dictionnaire des bonjour
##
class dict_hello:
	dictionary = None
	hello = []
	
	def __init__(self, file="hello.json"):
		with open(file) as hello_file:
			self.dictionary = json.load(hello_file)
		for i in self.dictionary.values():
			for j in i:
				self.hello.append(j)

class hello:
	hello_dict = dict_hello()

	def learn(self, string, language): #v 0.1.0
		if self.hello_dict.get(language) == None:
			return 1
		else:
			self.hello_dict.get(language).append(string)
			return 0
	##
	#	Dit si la phrase dans la string est une salutaion à partire du dictionnaire HELLO
	#	@param	str message = string à annalyser
	#	@return	bool
	##
	def isSay(self, message):
		isDetect = False
		for possibility in self.hello_dict.hello:
			if re.compile(r'\b({0})\b'.format(possibility), flags=re.IGNORECASE).search(message) != None:
				isDetect = True
				break
		
		return isDetect