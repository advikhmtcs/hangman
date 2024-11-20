import random

wordList = ("Counterrevolutionaries", "Deinstitutionalisation" ,"oligarchy", 'proletariet', 'Supercalifragilisticexpialidocious', 'Antidisestablishmentarianism' )
gameWord = wordList[random.randint(0,len(wordList)-1)]
gameLetters=[]
gameLetters.extend(gameWord)
underLines=[]
for i in range(len(gameWord)):
    underLines.append("_")
