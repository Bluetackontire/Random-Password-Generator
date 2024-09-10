import string, random, replit

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
punc = string.punctuation

while True:
  con = input("Press enter to continue")
  replit.clear()
  length = input("How long do you want your password (default 16 chacarters) \nEnter 0 to quit: ").strip()
  
  if length == "":
    for i in range(16):
      print(random.choice(lower + upper + num + punc), end="")
    print()
  elif int(length) == 0:
    print("Thank you for your time")
    break
  else:
    for i in range(int(length)):
      print(random.choice(lower + upper + num + punc), end="")
    print()