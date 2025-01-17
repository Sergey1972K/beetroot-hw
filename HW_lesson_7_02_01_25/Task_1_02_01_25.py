# Task 1
# program for creating dict where there are keys and the number of occurrences

def word_count_dict(text):
    words = text.split()
             
    my_dict = {}
    for word in words:
        if word in my_dict:
            my_dict[word] += 1  
        else:
            my_dict[word] = 1  
    return my_dict

text = input("Введіть текст: ")

result_dict = word_count_dict(text)

print("Підрахунок слів:", result_dict)