import spacy

nlp = spacy.load("en_core_web_lg")  # Load a small English language model

extracted_nouns = []


# Function to extract noun chunks from text
def extract_noun_chunks(text):
    doc = nlp(text)
    noun_phrases = []
    for chunk in doc.noun_chunks:
        if chunk[0].pos_ == "PRON":
            continue
        quantity = "0"
        noun_part = []
        firstPartToken = chunk[0]
        secondPartToken = chunk[1:] if chunk[1:] is not None else ""
        if firstPartToken.pos_ == "NUM":
            if firstPartToken.is_digit:
                quantity = firstPartToken.text
            else:
                quantity = "0"
                noun_part.append(firstPartToken.text)
        else:
            quantity = "0"
            noun_part.append(firstPartToken.text)
        noun_part.append(secondPartToken.text)
        noun = " ".join(noun_part)
        noun_phrases.append({"item": noun, "quantity": quantity})
    return noun_phrases


# Example text
# text = "chamfer, some Chairs, 4 4\" drill bits and 3 2x4x16' lumber boards."

# # Extract noun chunks
# extracted_nouns = extract_noun_chunks(text)
# # extracted_quantity = extract_quantity(text)
# print(extracted_nouns)
