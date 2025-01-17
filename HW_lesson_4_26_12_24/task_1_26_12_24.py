# String manipulation

text = "my"
print(text)

text_new = (text[:2]+text[-2:])
text_len = len(text)
if text_len >= 2:
    print(text_new)
if text_len < 2:
    print("Empty String")
