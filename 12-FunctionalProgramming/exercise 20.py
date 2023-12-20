text = 'I completely agree with you'
text2 = text.split()
result = f'No. of letters in words {list((map((lambda text2: len(text2)), text2)))}'
print(result)

list(map(lambda w: len(w), text.split()))