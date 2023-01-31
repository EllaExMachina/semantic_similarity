import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2= nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

#cat and monkey are similar as both are animals 
#monkey and banana have a higher similarity than banana and cat
#the model puts together that monkeys eat bananas and that is why there is more similarity.

tokens = nlp('cat apple monkey banana')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"

sentences = ["Where did my dog go", 
"Hello, there is my car",
"I\'ve lost my care in my car",
"I\'d like my boat back,",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similiarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similiarity)

#my own example for word similarities 
word1 = nlp("cat")
word2= nlp("monkey")
word3 = nlp("apple")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

#apple and monkey more similar than apple and cat
#perhaps because monkey and banana are linked as described above

#using en_core_web_sm
import spacy
nlp = spacy.load('en_core_web_sm')

word1 = nlp("cat")
word2= nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

#in en_core_web_sm similarity for all words is higher 
#monkey banana are more similar than monkey cat 

