import spacy

# Download and install the spaCy model if not already installed
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    # If the model is not found, download it
    from spacy.cli.download import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def perform_ner(text):
    # Process the input text with spaCy
    doc = nlp(text)

    # Print named entities and their labels
    for ent in doc.ents:
        print(f"Entity: {ent.text}, Label: {ent.label_}")

# Example text
sample_text = "Apple Inc. is a technology company headquartered in Cupertino, California. Steve Jobs co-founded Apple in 1976."

# Perform named entity recognition on the example text
perform_ner(sample_text)
