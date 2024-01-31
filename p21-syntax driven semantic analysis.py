import spacy

nlp = spacy.load("en_core_web_sm")

def extract_noun_phrases(sentence):
    doc = nlp(sentence)

    noun_phrases = []
    meanings = []

    for chunk in doc.noun_chunks:
        noun_phrases.append(chunk.text)
        meanings.append(chunk.text)

    return noun_phrases, meanings
sentence = "The quick brown fox jumped over the lazy dog."

noun_phrases, meanings = extract_noun_phrases(sentence)

print("Sentence:", sentence)
print("Noun Phrases:")
for phrase in noun_phrases:
    print(phrase)
print("Meanings:")
for meaning in meanings:
    print(meaning)
