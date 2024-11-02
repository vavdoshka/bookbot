def count_words_in_text(text):
    return len(text.split())

def count_characters_in_text(text):
    counters = {}
    text = text.lower()
    for ch in text:
        if ch not in counters:
            counters[ch] = 0
        counters[ch] += 1
    return counters

def read_text(document_name):
    with open(document_name) as f:
        text = f.read()
        return text

def sort_charecter_counters(charecter_counters):
    counters_list = []
    for k,v in charecter_counters.items():
        counters_list.append({
            "ch": k,
            "count": v
        })
    counters_list.sort(reverse=True, key=lambda x: x["count"])
    return counters_list

def print_report(document_name, words_len, character_counters):
    print(f"--- Begine report of {document_name} ---")
    print(f"{words_len} words found in the document")
    print()
    character_counters_list = sort_charecter_counters(character_counters)
    for item in character_counters_list:
        if item["ch"].isalpha():
            print(f"The '{item['ch']}' character was found {item['count']} times")
    print("--- End report ---")

def main():
    document_name = "books/frankenstein.txt"
    t = read_text(document_name)
    character_counters = count_characters_in_text(t)
    words_len = count_words_in_text(t)
    print_report(document_name, words_len, character_counters)

main()