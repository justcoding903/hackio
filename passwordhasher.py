import string
import random
def randomString(stringLength):
  letters = string.ascii_letters
  return ''.join(random.choice(letters) for i in range (stringLength))
def encrypt(integer):
  print(randomString(integer))
