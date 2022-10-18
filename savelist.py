import os

def save(list, file):
  f = open(file, "w")
  for x in range(len(list)):
    f.write(str(list[x]) + "\n")
  f.close()
def load(file):
  f = open(file, "r")
  return f.read().split("\n")