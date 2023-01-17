# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

long_string = 'авб абв бав абв вба бав вба абв абв абв авб бав вба бав вба'
long_string = ' '.join(list(filter(lambda elem: 'абв' not in elem.lower(), long_string.split())))
print(long_string)