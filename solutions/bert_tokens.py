# bert_tokens.py

# Load BERT tokenizer in
from transformers import BertTokenizer

# Initialize the tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

def get_tokens(string):
    '''Tokenize the input string with BERT'''
    tokens = tokenizer.tokenize(string)
    print(f"Texto: {string}")
    print(f"Tokens: {tokens}\n")

# Abbreviations
get_tokens('dlab')

# OOV (Out Of Vocabulary)
get_tokens('covid')

# Prefix
get_tokens('huggable')

# Digits
get_tokens('378')

# Your own example
get_tokens('grupo11')
