from gingerit.gingerit import GingerIt

text = input("Enter the string:")   #Input make sure to enter wrong string

parser = GingerIt()
main_dictionary = parser.parse(text)  #parsing string into dictionary"

original_text = main_dictionary["text"]   #mining original input text from dictionary print(text) will have no difference"
correction = main_dictionary["result"]     #mining corrected string from dictionmain_dictionaryry"

"""
You can also view whole dictionary through
print(main_dictionary)
"""

print("Original string is".center(50,"*"))
print(f"{original_text}")
print("Corrected string is".center(50,"*"))
print(f"{correction}")
"""
center() is used to align text in center and * is used to occupy vacant area
You can also ignore filling vacant area
"""

new_dictionary = main_dictionary["corrections"]
#main_dictionary has 2 dictionaries in it so breaking it for deeper resources dictionary 2/3

lenth_of_corrections = len(new_dictionary)
#finding length of dictionary for iteration
print(f"Total changes found {lenth_of_corrections}")

print("Changes Committed".center(40, '#'))

for i in range(lenth_of_corrections):
    final_dictionary = new_dictionary[i] #Breaking third and last dictionary
    original = final_dictionary["text"]  #wrong word
    corrected = final_dictionary["correct"]  #corrected word
    meaning = final_dictionary["definition"] #getting meaning of the word
    if meaning == None:
        meaning = "not found"

    print(f"'{original}' changed to {corrected} and definition '{meaning}'")
