
def main():
   frequency = computations()
   while True:
     while frequency == -1:
       frequency = computations()
     menu()
     # This is to check if the choice is valid
     choice = input("Please enter your choice: ")
     choice = valid_choice(choice)
     if choice == 1: 
        display_word_frequency(frequency)
     elif choice == 2:
        frequent = the_most_frequent_word(frequency)
        for item in frequent: 
           print(item)
     elif choice == 3:
        seach_word_and_display_frequency(frequency)
     elif choice == 4:
        print("Thank you for using our Word Counting System")
        break
    


def menu(): 
    width = 50
    print("*"* width)
    print("Welcome To Our Word Frequency Counter".center(width))
    print("*"* width)
    x = ["1 - Word frequency",
         "2 - The most frequent word",
         "3 - Search a word frequency",
         "4 - Exit"
    ]
    for item in x:
        print(item)
    print("*" * width)

def valid_choice(choice):
    while True:
        if choice in ["1","2","3","4"]:
            return int(choice) 
        else:
            choice = input("Please Enter a valid choice: ")
  
def computations():
   list_of_words = turn_into_list()
   cleaned = clean_text(list_of_words)
   frequency = count_times_word_appear(cleaned)
   return frequency
        
def turn_into_list():
    para = input("Enter a sentence or a paragraph: ")
    while not para.strip():
       print("You entered an empty sentence ")
       para = input("Please enter a sentence:")
    list_of_words = para.split() # split the words by the spaces and assign to a list
    # converts all words to lower case 
    for i  in range(len(list_of_words)): 
        new_item = list_of_words[i].lower()
        list_of_words[i] = new_item
    return list_of_words


def clean_text(list_of_words):
    # to clean punctuation from the word 
    clean_text = []
    for word in list_of_words: 
        if word.isalnum(): # isalnum() is meant to check if a character is a digit or a string 
            clean_text.append(word)
        else: 
            clean_word = ""
            for character in word: 
                if character.isalnum(): 
                    clean_word += character
                else: 
                    continue
            if clean_word.split(): # check if the the word is not empty
               clean_text.append(clean_word)
            else: 
                continue
    return clean_text

        
# count how many times a word appears 



def count_times_word_appear(list_of_words): # count frequency
    if len(list_of_words) == 0:
        print("There is no valid word in your paragraph")
        return - 1 # if the list of words is empty it returns - 1 
    else:
      frequency = {}
      for item in list_of_words:
        if item in frequency.keys(): 
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency 
 
        
# Display each unique word and its frequency.
def display_word_frequency(frequency_of_words_dict): # display word frequency 
    for k,v in frequency_of_words_dict.items(): 
       print(f"{k}:{v}") 

def the_most_frequent_word(dict_of_words):# find the most frequent word 
   highest_frequency = max(dict_of_words.values())
   if highest_frequency == 1: 
      print("No words occur more frequently than others")
      return []
   frequent = []
   for k,v in dict_of_words.items():
      if v == highest_frequency:
        frequent.append((k,v))
   return frequent
   
        

def seach_word_and_display_frequency(frequency): 
    word = input("Enter the word you want to search for: ")
    if word.strip(): 
       result = frequency.get(word.lower().strip(),None)
       if result != None: 
          print(f"The frequency of the word '{word}' is {result}")
       else:
         print(f"The word '{word}' was not found")
    else:
        print("You didn't enter a word")


main()






        
        
     

