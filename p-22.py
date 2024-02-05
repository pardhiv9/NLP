import spacy

def perform_reference_resolution(text):
    # Load the spaCy English model
    nlp = spacy.load("en_core_web_sm")

    # Process the input text with spaCy
    doc = nlp(text)

    # Perform reference resolution
    resolved_text = []
    current_entity = None

    for token in doc:
        if token.dep_ in ["nsubj", "nsubjpass", "dobj", "attr"]:
            # If the token is a subject or object, consider it as a potential entity
            current_entity = token.text
        elif token.dep_ == "pron" and current_entity:
            # If the token is a pronoun and there is a current entity, replace the pronoun with the entity
            resolved_text.append(current_entity)
            current_entity = None
        else:
            # Otherwise, keep the original token
            resolved_text.append(token.text)

    # Print the resolved text
    print(" ".join(resolved_text))

# Example text with references
sample_text = "John is a software engineer. He loves programming and works for a tech company."

# Perform reference resolution on the example text
perform_reference_resolution(sample_text)
