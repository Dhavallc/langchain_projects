import json
import tiktoken
import sys

def count_tokens_in_file(file_path, model='cl100k_base'):
    enc = tiktoken.get_encoding(model)
    total_tokens = 0
    total_items = 0

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        if 'embedding_text' in item:
            tokens = enc.encode(item['embedding_text'])
            token_count = len(tokens)
            total_tokens += token_count
            total_items += 1
        else:
            print("Missing embedding_text")

    print(f"\n Processed {total_items} items")
    print(f"Total tokens in 'embedding_text': {total_tokens}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_tokens.py <path-to-json>")
    else:
        count_tokens_in_file(sys.argv[1])
