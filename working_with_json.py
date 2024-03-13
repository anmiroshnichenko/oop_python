import json
import collections
def read_json(file_path, word_max_len=6, top_words_amt=10):
    # Мое решение    
    with open('newsafr.json', 'r') as f: # открокрыть файл на чтение
        json_date = json.load(f)
    all_words = ""
    for new in json_date['rss']['channel']['items']:    
        all_words += new['description']
    words = all_words.split()
    list_words = []
    for word in words:
        if len(word) > word_max_len:
            list_words.append(word)
    unique_words = set(list_words)
    top_words = dict()    
    for w in unique_words:
        top_words[w] = list_words.count(w)      
    sorted_top_words = sorted(top_words.items(), key=lambda item: item[1], reverse=True)[0:10]
    words_top = []
    for wr in sorted_top_words:   
        words_top.append(wr[0])
    return words_top

# # Решение эксперта
    with open(file_path, 'r', encoding='utf-8') as news_file:
        news = json.load(news_file)
        description_words = []
        for item in news['rss']['channel']['items']:
            description = [word for word in item['description'].split(' ') if len(word) > word_max_len]
            description_words.extend(description)
        words_counter = collections.Counter(description_words)
        popular_words = [w[0] for w in words_counter.most_common(top_words_amt)]
        return popular_words



if __name__ == '__main__':
    print(read_json('newsafr.json'))