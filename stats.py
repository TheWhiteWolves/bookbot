from operator import itemgetter

def get_num_words(text):
    return len(text.split())

def get_num_characters(text):
    count = {}
    for letter in text:
        letter = letter.lower()
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    return count

def sort_characters(characters):
    list = []
    for k, v in characters.items():
        list.append({"char":k, "num":v})
    list.sort(key=itemgetter('num'), reverse=True)
    return list