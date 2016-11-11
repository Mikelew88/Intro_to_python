def parse(text):
  '''
  Write a function that takes a text string, and returns the number of words and characters in it

  Input:    (1) string, text to be parsed

  Output:   (1) tuple, (number of words, number of characters)
  '''
  word_count = 0
  char_count = 0
  for word in text.split():
      word_count+=1
      for char in word:
          char_count+=1

  return (word_count,char_count)

if __name__ == '__main__':
    print parse('Hello World')
