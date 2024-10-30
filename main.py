import random

wordList = ("Counterrevolutionaries", "Deinstitutionalisation" ,"oligarchy", 'proletariet', 'Supercalifragilisticexpialidocious', 'Antidisestablishmentarianism' )
gameWord = wordList[random.randint(0,len(wordList)-1)]
print(gameWord)