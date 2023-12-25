from flask import Flask,render_template,request
from PBL import getNumberOfSentences,getNumberOfParagraph,getNumberOfWords,getWordsPerSentence,getCharacters,getCharPerWords
app=Flask(__name__)



@app.route("/",methods=["GET","POST"])
def hello_world():
    if request.method=="POST":
        paragraph=request.form.get('subject')
        if paragraph.strip()!='':
            no_of_sentence=getNumberOfSentences(paragraph)
            no_of_Paragraph = getNumberOfParagraph(paragraph)
            no_of_Words = getNumberOfWords(paragraph)
            Words_per_sentence = getWordsPerSentence(paragraph)
            no_of_Character = getCharacters(paragraph)
            no_of_Character_with_space = getCharacters(paragraph,including_space=True)
            Character_per_word = getCharPerWords(paragraph)
            return render_template("PBL Framwork.html",no_of_sentence=no_of_sentence,no_of_Paragraph=no_of_Paragraph,no_of_Words=no_of_Words,Words_per_sentence=Words_per_sentence, no_of_Character=no_of_Character,Character_per_word=Character_per_word, no_of_Character_with_space=no_of_Character_with_space)
    return render_template("PBL Framwork.html")

if __name__=="__main__":
    app.run()