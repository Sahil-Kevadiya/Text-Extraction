from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords

#str = input("Enter the String : ")
str = '''This is a small demonstration .pdf file - 
 just for use in the Virtual Mechanics tutorials. More text. And more 
 text. And more text. And more text. And more text. 
 And more text. And more text. And more text. And more text. And more 
 text. And more text. Boring, zzzzz. And more text. And more text. And 
 more text. And more text. And more text. And more text. And more text. 
 And more text. And more text. 
 And more text. And more text. And more text. And more text. And more 
 text. And more text. And more text. Even more. Continued on page 2 ...'''
#print(str)
#print("After Split")

a = str.split()
#print(a)
	
def removePunctuation(word_list):
    punctuations='''!()-[]{};:'’"\,<>./?@#$%^&*_~'''
    new_list=[]
    for word in word_list:
        temp_word=""
        for char in word:
            if char in punctuations:
                temp_word+=''
            else:
                temp_word+=char
        if temp_word.strip()!='':
            new_list.append(temp_word)
    return new_list

def removeStopWords(word_list):
    stop_words=stopwords.words('english')
    new_list=[]
    for i in word_list:
        if i.strip().lower() in stop_words:
            continue
        new_list.append(i.strip())
    
    return new_list
def getNumberOfSentences(txt):
    return len(sent_tokenize(txt))

def getNumberOfWords(txt):
    return len(removePunctuation(word_tokenize(txt)))

def getWordsPerSentence(txt):
    words_per_sentences=[]
    sentances=sent_tokenize(txt)
    for i in sentances:
        words_per_sentences.append(getNumberOfWords(i))
    return "{:.2f}".format(sum(words_per_sentences)/len(words_per_sentences))

def getCharPerWords(txt):
    char_per_words=[]
    words=word_tokenize(txt)
    for i in words:
        char_per_words.append(getCharacters(i,including_space=True))
    return "{:.2f}".format(sum(char_per_words)/len(char_per_words))

def getCharacters(txt,including_space=False):
    count=0
    if including_space:
        return len(txt)
    for i in txt:
        if i!=' ':
            count+=1
    return count

def getNumberOfParagraph(txt):
    count=1
    for i in range(len(txt)):
        if txt[i]=='\n':
            if i+1<len(txt):
                if txt[i+1]!='\n':
                    count+=1
    return count

def getWordFrequencyList(word_list):
    freq_list=[]
    unique_words=set(word_list)
    for i in unique_words:
        freq_list.append([i,word_list.count(i)])
    
    return sorted(freq_list,key=lambda x:x[1],reverse=True)

			

if __name__=="__main__":
    print("Number of Sentences :",getNumberOfSentences(str))
    print("Number of Paragraph :",getNumberOfParagraph(str))
    print("Number of Words :",getNumberOfWords(str))
    print("Word Per Sentence :",getWordsPerSentence(str))
    print("Number of Characters excluding Space :",getCharacters(str))
    print("Number of Characters including Space :",getCharacters(str,including_space=True))
    print("Characters per Word :",getCharPerWords(str)) 