import time


# load dictionary words from file
def load_words():
  all_words = []
  start_time = time.time()
  
  with open('safedict_simple.txt', 'r') as f:
    for line in f:
      all_words.append(line.rstrip())
  end_time = time.time()

  elapsed_time = end_time - start_time
  # log words loaded and elapsed time
  print('Loaded ' + str(len(all_words)) + ' words in ' + f'{elapsed_time:.2f}' + ' seconds.')

  return all_words


def suggest(text, all_words):

  text = input('')

#   # YOUR CODE HERE. This currently doesn't suggest a correction, just checks if the input is already a word. You'll want to change that 

  if text in all_words:
    print(text + ' is a word')
  else:
   print(text + ' is not a word, look for words that start with') 

  # Insert code above that tells user word is not a word while also inserting suggestion which the user then can type after


def main():
  all_words = load_words()
  print('Type some text, or type \"quit\" to stop')
  while True:
      user_word = input('Enter word here --> ')
      text = user_word

      """
      start of my code
      """ 

      list_of_letters = list(text)
      length = len(list_of_letters)
      middle_index = length//2
      first_half = list_of_letters[:middle_index]
      look_for = (''.join(first_half))
      if text in all_words:
        print("this is already a word")
      else:
        print("this isnt a word, look for words that start with - " + look_for)

      #try to add a comparison function for the user input and words defined in dictionary to print out for user to type

      """
      end of my code
      """


      if ('quit' == text):
        break
      suggest(text, all_words)



if __name__ == "__main__":
    main()