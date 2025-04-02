lang1 = "Python"
lang2 = "C++"
lang3 = "Java"
lang4 = "Pascal"
author1 = "Guido van Rossum"
author2 = "Bjatne Stroustrup"
author3 = "jame Gosling"
author4 = "Niklaus Wirth"
line = "#"*25
sep = ' : '
# print ("#"*25)
# print (lang1, author1, sep=sep)
# print (lang2, author2, sep=sep)
# print (lang3, author3, sep=sep)
# print (lang4, author4, sep=sep)
# print (line)


'''
print (line)
print (f"{py} : {pyn} ")
print (f"   {c} : {cn} ")
print (f"  {ja} : {jan} ")
print (f"{pa} : {pan} ")
print (line)
'''


print (line)
print (f"{lang1:>6}{sep}{author1}")
print (f"{lang2:>6}{sep}{author2}")
print (f"{lang3:>6}{sep}{author3}")
print (f"{lang4:>6s}{sep}{author4}")
print (line)
