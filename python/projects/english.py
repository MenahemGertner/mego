# a = [input() for i in range(int(input()))]
# print(a)
import webbrowser

opening = '''                /|  /|  ---------------------------
                ||__||  |  Welcome to the program  |
               /   O O\__  for learning the 1,000  |
              /          \ useful words in English |
             /      \     \        easily!         |
            /   _    \     \ ----------------------
           /    |\____\     \      ||
          /     | | | |\____/      ||
         /       \| | | |/ |     __||
        /  /  \   -------  |_____| ||
       /   |   |           |       --|
       |   |   |           |_____  --|
       |  |_|_|_|          |     \----
       /\                  |
      / /\        |        /
     / /  |       |       |
 ___/ /   |       |       |
|____/    c_c_c_C/ \C_c_c_c'''

welcome = '''  (¯`·.¸¸.·´¯`·.¸¸.·´¯)
  ( \                 / )
 ( \ )               ( / )
( ) (    Welcome!!    ) ( )
 ( / )               ( \ )
  ( /                 \ )
   (_.·´¯`·.¸¸.·´¯`·.¸_)'''

welcome_back = '''  (¯`·.¸¸.·´¯`·.¸¸.·´¯)
  ( \                 / )
 ( \ )               ( / )
( ) (  Welcome back!! ) ( )
 ( / )               ( \ )
  ( /                 \ )
   (_.·´¯`·.¸¸.·´¯`·.¸_)'''

remote = '''           ⇓ After learning the meaning of the word ⇓
 -----------------------------------------------------------------
| Read the last words in English and its interpretation in Hebrew |
|    and vice versa, read in Hebrew and translate to English!     |
 -----------------------------------------------------------------'''

words = ['ability', 'able', 'about', 'above', 'accept', 'according', 'account', 'across', 'act', 'action', 'activity',
         'actually', 'add', 'address', 'administration', 'admit', 'adult', 'affect', 'after', 'again', 'against', 'age',
         'agency', 'agent', 'ago', 'agree', 'agreement', 'ahead', 'air', 'all', 'allow', 'almost', 'alone', 'along',
         'already', 'also', 'although', 'always', 'American', 'among', 'amount', 'analysis', 'and', 'animal', 'another',
         'answer', 'any', 'anyone', 'anything', 'appear', 'apply', 'approach', 'area', 'argue', 'arm', 'around',
         'arrive', 'art', 'article', 'artist', 'as', 'ask', 'assume', 'at', 'attack', 'attention', 'attorney',
         'audience', 'author', 'authority', 'available', 'avoid', 'away', 'baby', 'back', 'bad', 'bag', 'ball', 'bank',
         'bar', 'base', 'be', 'beat', 'beautiful', 'because', 'become', 'bed', 'before', 'begin', 'behavior', 'behind',
         'believe', 'benefit', 'best', 'better', 'between', 'beyond', 'big', 'bill', 'billion', 'bit', 'black', 'blood',
         'blue', 'board', 'body', 'book', 'born', 'both', 'box', 'boy', 'break', 'bring', 'brother', 'budget', 'build',
         'building', 'business', 'but', 'buy', 'by', 'call', 'camera', 'campaign', 'can', 'cancer', 'candidate',
         'capital', 'car', 'card', 'care', 'career', 'carry', 'case', 'catch', 'cause', 'cell', 'center', 'central',
         'century', 'certain', 'certainly', 'chair', 'challenge', 'chance', 'change', 'character', 'charge', 'check',
         'child', 'choice', 'choose', 'church', 'citizen', 'city', 'civil', 'claim', 'class', 'clear', 'clearly',
         'close', 'coach', 'cold', 'collection', 'college', 'color', 'come', 'commercial', 'common', 'community',
         'company', 'compare', 'computer', 'concern', 'condition', 'conference', 'Congress', 'consider', 'consumer',
         'contain', 'continue', 'control', 'cost', 'could', 'country', 'couple', 'course', 'court', 'cover', 'create',
         'crime', 'cultural', 'culture', 'cup', 'current', 'customer', 'cut', 'dark', 'data', 'daughter', 'day', 'dead',
         'deal', 'death', 'debate', 'decade', 'decide', 'decision', 'deep', 'defense', 'degree', 'Democrat',
         'democratic', 'describe', 'design', 'despite', 'detail', 'determine', 'develop', 'development', 'die',
         'difference', 'different', 'difficult', 'dinner', 'direction', 'director', 'discover', 'discuss', 'discussion',
         'disease', 'do', 'doctor', 'dog', 'door', 'down', 'draw', 'dream', 'drive', 'drop', 'drug', 'during', 'each',
         'early', 'east', 'easy', 'eat', 'economic', 'economy', 'edge', 'education', 'effect', 'effort', 'eight',
         'either', 'election', 'else', 'employee', 'end', 'energy', 'enjoy', 'enough', 'enter', 'entire', 'environment',
         'environmental', 'especially', 'establish', 'even', 'evening', 'event', 'ever', 'every', 'everybody',
         'everyone', 'everything', 'evidence', 'exactly', 'example', 'executive', 'exist', 'expect', 'experience',
         'expert', 'explain', 'eye', 'face', 'fact', 'factor', 'fail', 'fall', 'family', 'far', 'fast', 'father',
         'fear', 'federal', 'feel', 'feeling', 'few', 'field', 'fight', 'figure', 'fill', 'film', 'final', 'finally',
         'financial', 'find', 'fine', 'finger', 'finish', 'fire', 'firm', 'first', 'fish', 'five', 'floor', 'fly',
         'focus', 'follow', 'food', 'foot', 'for', 'force', 'foreign', 'forget', 'form', 'former', 'forward', 'four',
         'free', 'friend', 'from', 'front', 'full', 'fund', 'future', 'game', 'garden', 'gas', 'general', 'generation',
         'get', 'girl', 'give', 'glass', 'go', 'goal', 'good', 'government', 'great', 'green', 'ground', 'group',
         'grow', 'growth', 'guess', 'gun', 'guy', 'hair', 'half', 'hand', 'hang', 'happen', 'happy', 'hard', 'have',
         'he', 'head', 'health', 'hear', 'heart', 'heat', 'heavy', 'help', 'her', 'here', 'herself', 'high', 'him',
         'himself', 'his', 'history', 'hit', 'hold', 'home', 'hope', 'hospital', 'hot', 'hotel', 'hour', 'house', 'how',
         'however', 'huge', 'human', 'hundred', 'husband', 'I', 'idea', 'identify', 'if', 'image', 'imagine', 'impact',
         'important', 'improve', 'in', 'include', 'including', 'increase', 'indeed', 'indicate', 'individual',
         'industry', 'information', 'inside', 'instead', 'institution', 'interest', 'interesting', 'international',
         'interview', 'into', 'investment', 'involve', 'issue', 'it', 'item', 'its', 'itself', 'job', 'join', 'just',
         'keep', 'key', 'kid', 'kill', 'kind', 'kitchen', 'know', 'knowledge', 'land', 'language', 'large', 'last',
         'late', 'later', 'laugh', 'law', 'lawyer', 'lay', 'lead', 'leader', 'learn', 'least', 'leave', 'left', 'leg',
         'legal', 'less', 'let', 'letter', 'level', 'lie', 'life', 'light', 'like', 'likely', 'line', 'list', 'listen',
         'little', 'live', 'local', 'long', 'look', 'lose', 'loss', 'lot', 'love', 'low', 'machine', 'magazine', 'main',
         'maintain', 'major', 'majority', 'make', 'man', 'manage', 'management', 'manager', 'many', 'market',
         'marriage', 'material', 'matter', 'may', 'maybe', 'me', 'mean', 'measure', 'media', 'medical', 'meet',
         'meeting', 'member', 'memory', 'mention', 'message', 'method', 'middle', 'might', 'military', 'million',
         'mind', 'minute', 'miss', 'mission', 'model', 'modern', 'moment', 'money', 'month', 'more', 'morning', 'most',
         'mother', 'mouth', 'move', 'movement', 'movie', 'Mr', 'Mrs', 'much', 'music', 'must', 'my', 'myself', 'name',
         'nation', 'national', 'natural', 'nature', 'near', 'nearly', 'necessary', 'need', 'network', 'never', 'new',
         'news', 'newspaper', 'next', 'nice', 'night', 'no', 'none', 'nor', 'north', 'not', 'note', 'nothing', 'notice',
         'now', "n't", 'number', 'occur', 'of', 'off', 'offer', 'office', 'officer', 'official', 'often', 'oh', 'oil',
         'ok', 'old', 'on', 'once', 'one', 'only', 'onto', 'open', 'operation', 'opportunity', 'option', 'or', 'order',
         'organization', 'other', 'others', 'our', 'out', 'outside', 'over', 'own', 'owner', 'page', 'pain', 'painting',
         'paper', 'parent', 'part', 'participant', 'particular', 'particularly', 'partner', 'party', 'pass', 'past',
         'patient', 'pattern', 'pay', 'peace', 'people', 'per', 'perform', 'performance', 'perhaps', 'period', 'person',
         'personal', 'phone', 'physical', 'pick', 'picture', 'piece', 'place', 'plan', 'plant', 'play', 'player', 'PM',
         'point', 'police', 'policy', 'political', 'politics', 'poor', 'popular', 'population', 'position', 'positive',
         'possible', 'power', 'practice', 'prepare', 'present', 'president', 'pressure', 'pretty', 'prevent', 'price',
         'private', 'probably', 'problem', 'process', 'produce', 'product', 'production', 'professional', 'professor',
         'program', 'project', 'property', 'protect', 'prove', 'provide', 'public', 'pull', 'purpose', 'push', 'put',
         'quality', 'question', 'quickly', 'quite', 'race', 'radio', 'raise', 'range', 'rate', 'rather', 'reach',
         'read', 'ready', 'real', 'reality', 'realize', 'really', 'reason', 'receive', 'recent', 'recently',
         'recognize', 'record', 'red', 'reduce', 'reflect', 'region', 'relate', 'relationship', 'religious', 'remain',
         'remember', 'remove', 'report', 'represent', 'Republican', 'require', 'research', 'resource', 'respond',
         'response', 'responsibility', 'rest', 'result', 'return', 'reveal', 'rich', 'right', 'rise', 'risk', 'road',
         'rock', 'role', 'room', 'rule', 'run', 'safe', 'same', 'save', 'say', 'scene', 'school', 'science',
         'scientist', 'score', 'sea', 'season', 'seat', 'second', 'section', 'security', 'see', 'seek', 'seem', 'sell',
         'send', 'senior', 'sense', 'series', 'serious', 'serve', 'service', 'set', 'seven', 'several', 'sex', 'sexual',
         'shake', 'share', 'she', 'shoot', 'short', 'shot', 'should', 'shoulder', 'show', 'side', 'sign', 'significant',
         'similar', 'simple', 'simply', 'since', 'sing', 'single', 'sister', 'sit', 'site', 'situation', 'six', 'size',
         'skill', 'skin', 'small', 'smile', 'so', 'social', 'society', 'soldier', 'some', 'somebody', 'someone',
         'something', 'sometimes', 'son', 'song', 'soon', 'sort', 'sound', 'source', 'south', 'southern', 'space',
         'speak', 'special', 'specific', 'speech', 'spend', 'sport', 'spring', 'staff', 'stage', 'stand', 'standard',
         'star', 'start', 'state', 'statement', 'station', 'stay', 'step', 'still', 'stock', 'stop', 'store', 'story',
         'strategy', 'street', 'strong', 'structure', 'student', 'study', 'stuff', 'style', 'subject', 'success',
         'successful', 'such', 'suddenly', 'suffer', 'suggest', 'summer', 'support', 'sure', 'surface', 'system',
         'table', 'take', 'talk', 'task', 'tax', 'teach', 'teacher', 'team', 'technology', 'television', 'tell', 'ten',
         'tend', 'term', 'test', 'than', 'thank', 'that', 'the', 'their', 'them', 'themselves', 'then', 'theory',
         'there', 'these', 'they', 'thing', 'think', 'third', 'this', 'those', 'though', 'thought', 'thousand',
         'threat', 'three', 'through', 'throughout', 'throw', 'thus', 'time', 'to', 'today', 'together', 'tonight',
         'too', 'top', 'total', 'tough', 'toward', 'town', 'trade', 'traditional', 'training', 'travel', 'treat',
         'treatment', 'tree', 'trial', 'trip', 'trouble', 'true', 'truth', 'try', 'turn', 'TV', 'two', 'type', 'under',
         'understand', 'unit', 'until', 'up', 'upon', 'us', 'use', 'usually', 'value', 'various', 'very', 'victim',
         'view', 'violence', 'visit', 'voice', 'vote', 'wait', 'walk', 'wall', 'want', 'war', 'watch', 'water', 'way',
         'we', 'weapon', 'wear', 'week', 'weight', 'well', 'west', 'western', 'what', 'whatever', 'when', 'where',
         'whether', 'which', 'while', 'white', 'who', 'whole', 'whom', 'whose', 'why', 'wide', 'wife', 'will', 'win',
         'wind', 'window', 'wish', 'with', 'within', 'without', 'woman', 'wonder', 'word', 'work', 'worker', 'world',
         'worry', 'would', 'write', 'writer', 'wrong', 'yard', 'yeah', 'year', 'yes', 'yet', 'you', 'young', 'your',
         'yourself']
new_words = []
old_word = 0
num = 0
back = 0


# Opening text and explanation of the program
print(f"\n{opening}")
run = input("\nFeeling ready? Press Enter to begin!"
            "\nIf you want to continue from the point where you left the program press 'y': ")
if run == "":
    print(f"\n\n{welcome}")

# Return to the program from the last word of the previous use
else:
    back = int(input(f"\n\n{welcome_back}\n\nEnter word index are you holding?: \n")) - 1
    num = back

# A loop to go through all the words in the list one by one
for i in range(back, len(words)):
    num += 1

    # A message of encouragement after 20 words from the list
    if i > 0 and i % 20 == 0:
        print(f"👏🏼👏🏼👏🏼 You already know '{i}' words from the list!!! 👏🏼👏🏼👏🏼")
    print(f"\nYour new word is:\n\n{num}. '{words[i]}'")
    know = input("\nDo you know this word? If yes press Enter. If you are not sure, press 'n'.\n\n")
    if know == "":
        print("\nGreat!👌\n")
    else:
        # Creating a list of the unfamiliar words for repetition and memorization
        new_words.append(words[i])
        old_word += 1

        # Instructions for memorizing the new words

        chak = input("Write the new word and you can get its translation: ")
        while True:
            if chak.casefold() == words[i]:
                break
            else:
                chak = input("Spell the word correctly again: ")

        # chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        # webbrowser.get(chrome_path).open(
        #     f"https://translate.google.co.il/?hl=iw&sl=en&tl=iw&text={words[i]}%0A&op=translate")

        # edge_path = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s'
        # webbrowser.get(edge_path).open(
        #     f"https://translate.google.co.il/?hl=iw&sl=en&tl=iw&text={words[i]}%0A&op=translate")

        webbrowser.open(f"https://translate.google.co.il/?hl=iw&sl=en&tl=iw&text={words[i]}%0A&op=translate")
        print(f"___________________________________________________________\n\n\n\n\n\n\n\n\n\n{remote}"
              f"\n\n\nThe last words: >>>>>----------------------->   '{', '.join(new_words[-3:])}'")
        if old_word >= 7:
            print("And also the old word: >>>>----------------->   '" + new_words[-7] + "'")

        print(f"\n\n           If you forgot the meaning of one of the words,"
              f"\nyou can write it down here and get its translation, Otherwise press Enter"
              f"\n      ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓")
        translate = input()

        while True:
            if translate == "":
                break
            elif translate == "statistic":
                left = 1000 - num
                percentage = round((num - old_word) / num * 100)
                print(f"Words you have already learned: {num}"
                      f"\nWords still left: {left}"
                      f"\nNew words you learned: {old_word}"
                      f"\nPercentage of words you knew: {percentage}%\n")
                break
            else:
                webbrowser.open(f"https://translate.google.co.il/?hl=iw&sl=en&tl=iw&text={translate}%0A&op=translate")
                translate = input("You can check another word again. If you wish to continue press Enter ")

        print("\nExcellent! Now that you have memorized the word well, "
              "you can move on to the next word!👉")

        # A message of encouragement after learning 10 new words
        if old_word % 5 == 0:
            print(f"👏🏼👏🏼👏🏼 Wow!! Today you already learned '{old_word}' new words!!! 👏🏼👏🏼👏🏼")

# End of the program
print("Well done!! You have successfully learned all the words!!!!")
