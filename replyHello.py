import re
import json

HELLO = [
#Français|____________________|
	"yo",
	"hey",
	"bonjour",
	"bjr",
	"bonsoir",
	"salut",
	"slt",
	"salutation",
#English|_____________________|
	"hello",
	"hi",
	"good evening",
	"good night",
#Español|_____________________|
	"hola",
	"buenos dias",
	"buenos noches",
	"saludo",
#Deutsch|_____________________|
	"hallo",
	"gruß",
#Nihon|_______________________|
	"konichiwa",
	"ohayo",
#日本|________________________|
	"こんにちは",
	"おはよう",
#Esperanto|___________________|
	"saluton"
]

##
 #	Dit si la phrase dans la string est une salutaion à partire du dictionnaire HELLO
 #	@param	str message = string à annalyser
 #	@return	bool
##
def isSayHello(message):
	isDetect = False	
	for possibility in HELLO:
		if re.compile(r'\b({0})\b'.format(possibility), flags=re.IGNORECASE).search(message) != None:
			isDetect = True
			break
	
	return isDetect