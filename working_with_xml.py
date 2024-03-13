# Мое решение
# import xml.etree.ElementTree as ET
# def read_xml(file_path, word_max_len=6, top_words_amt=10):
#     parser = ET.XMLParser(encoding='utf-8')
#     tree = ET.parse('newsafr.xml', parser) 
#     root = tree.getroot()
#     descriptions_list = root.findall('channel/item/description')  
#     descriptions_words = []
#     for descriptions in descriptions_list:
#          description = [word for word in descriptions.text.split(' ') if len(word) > word_max_len]   
#          descriptions_words.extend(description)
#     unique_words = set(descriptions_words)
#     top_words = dict()    
#     for w in unique_words:
#         top_words[w] = descriptions_words.count(w)      
#     sorted_top_words = sorted(top_words.items(), key=lambda item: item[1], reverse=True)[0:10]
#     words_top = []
#     for wr in sorted_top_words:   
#         words_top.append(wr[0])
#     return words_top 
    
# if __name__ == '__main__':
#     print(read_xml('newsafr.xml'))

# Решение эсперта
import collections
import xml.etree.ElementTree as ET

def read_xml(file, len_word=6, top_words=10):
    tree = ET.parse(file)
    root = tree.getroot()
    xml_items = root.findall('channel/item')
    description_words = []
    descriptions = [item.find('description').text.split() for item in xml_items]
    for description in descriptions:
        description = [word for word in description if len(word) > len_word]
        description_words.extend(description)
    words_counter = collections.Counter(description_words)
    popular_words = [w[0] for w in words_counter.most_common(top_words)]
    return popular_words


if __name__ == '__main__':
    print(read_xml('newsafr.xml'))   