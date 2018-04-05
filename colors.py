import sys
import os

def echo(msg):
  os.system('echo -n "' + str(msg) + '"')

def out(n):
  os.system("tput setab " + str(n) + "; echo -n " + ("\"% 4d\"" % n))
  os.system("tput setab 0")

# Tests 256 color output in terminal
def test_term_colors():
  # normal colors 1 - 16
  os.system("tput setaf 16")
  for n in range(8):
    out(n)
  echo("\n")
  for n in range(8, 16):
    out(n)

  echo("\n")
  echo("\n")

  y=16
  while y < 231:
    for z in range(0,6):
      out(y)
      y += 1
    echo("\n")

  echo("\n")

  for n in range(232, 256):
    out(n)
    if n == 237 or n == 243 or n == 249:
      echo("\n")

  echo("\n")
  os.system("tput setaf 7")
  os.system("tput setab 0")

if __name__ == "__main__":
  test_term_colors()
