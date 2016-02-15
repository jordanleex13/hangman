print "Hangman Game. You have 9 chances.\n"
import random
words = ["biology","explosion","pokemon","christmas","light","clavicle",
"cactus","ridge", "permit","simulator","electron","savant","arsenic", "construction",
"fated","lovers","destiny", "abbey", 'abruptly','affix','askew','axiom','azure',
'bagpipes','bandwagon','banjo','bayou','bikini','blitz','bookworm','boxcar','boxful',
'buckaroo','buffalo','buffoon','cobweb','croquet','daiquiri','disavow','duplex',
'dwarves','equip','exodus','fishhook','fixable','foxglove','galaxy','galvanize',
'gazebo','gizmo','glowworm','guffaw','haiku','haphazard','hyphen','icebox','injury',
'ivory','ivy','jaundice','jawbreaker','jaywalk','jazzy','jigsaw','jiujitsu','jockey',
'jovial','joyful','juicy','jumbo','kazoo','keyhole','khaki','kilobyte','kiosk','kiwifruit',
'knapsack','larynx','luxury','marquis','megahertz','microwave','mystify','nightclub',
'nowadays','numbskull','ovary','oxidize','oxygen','pajama','peekaboo','pixel','pizazz',
'pneumonia','polka','quartz','quiz','quorum','rhubarb','rickshaw',
'schizophrenia','sphinx','spritz','squawk','subway','swivel','topaz','unknown','unworthy',
'unzip','uptown','vaporize','vixen','vodka','vortex','walkway','waltz','wavy','waxy',
'wheezy','whiskey','whomever','wimpy','wizard','woozy','xylophone','yachtsman','yippee',
'youthful','zephyr','zigzag','zilch','zodiac','zombie']

secretWord = words[random.randrange(0,len(words),1)]
secretWord = secretWord.upper()

guess = ["_"]*len(secretWord)
tries = 0
guessedLetters = ""
found = False
while tries < 9 and found == False:

    while True:
        letter = raw_input("Pick a letter --> ")
        letter = letter.upper()

        if letter in guessedLetters:
            print "Already guessed %s\n" %letter
        elif letter.isalpha() == False:
            print "Not a letter\n"
        elif len(letter) > 1:
            print "Too many letters\n"
        else:
            guessedLetters = guessedLetters + " " + letter
            break

    print "Guessed Letters: " + guessedLetters

    foundletter = False
    for n in range(len(secretWord)):
        if letter == secretWord[n]:
            guess[n] = letter
            foundletter = True
        if n == len(secretWord)-1 and foundletter == False:
            tries += 1

    print "Failed times: %d" %tries

    found = True
    for n in range(len(guess)):
        if guess[n] == '_':
            found = False

    print guess
    print "\n"

if found == True:
    print "YOU WIN"
else:
    print "YOU LOSE! The secret word was %s" %secretWord
    
#Fine
