translate_dic = {}
palabras = input("Introduzca una palabra separada por : y su traducción, escriba pares separados por comas. ej. palabra:traducción: ")
trasnlate_list = palabras.split(",")
for translation in trasnlate_list:
    list_values = translation.split(":")
    translate_key = list_values[0]
    translate_value = list_values[1]
    translate_dic[translate_key] = translate_value

sentence = input("Introduzca una oraciòn: ")
sentence_list = sentence.split()
print("La traducción es:")
for word in sentence_list:
    if word in translate_dic:
        print(translate_dic[word], end=" ")
    else:
        print(word, end= " ")

