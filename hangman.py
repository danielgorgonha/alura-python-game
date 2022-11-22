

def play():
  print("**********************************")
  print("***Welcome to the hangman game!***")
  print("**********************************")

  palavra_secreta = "banana"

  enforcou = False
  acertou = False

  while(not enforcou and not acertou):

    chute = input("Qual letra? ")
    
    index = 0
    for letra in palavra_secreta:
      if(chute == letra):
        print("Encontrei a letra {} na possição {}".format(letra, index))
      index = index + 1
    
    print("jogando ...")

  print("End of the game")

if(__name__ == "__main__"):
  play()