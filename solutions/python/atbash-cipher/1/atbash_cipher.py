def five_grouper(text):
    new_text = " ".join([text[i:i+5] for i in range(0, len(text), 5)])
    return new_text

def encode(plain_text):
    plain_text = plain_text.lower()
    
    ENCODER_TRANSLATION_TABLE = plain_text.maketrans("abcdefghijklmnopqrstuvwxyz1234567890", "zyxwvutsrqponmlkjihgfedcba1234567890", " ,.")
    return plain_text.translate(ENCODER_TRANSLATION_TABLE) if len(plain_text) <= 5 else five_grouper(plain_text.translate(ENCODER_TRANSLATION_TABLE))


def decode(ciphered_text):
    ciphered_text = ciphered_text.lower()
    
    DECODER_TRANSLATION_TABLE = ciphered_text.maketrans("zyxwvutsrqponmlkjihgfedcba", "abcdefghijklmnopqrstuvwxyz", " ,.")
    return ciphered_text.translate(DECODER_TRANSLATION_TABLE)
