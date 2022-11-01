import guessing
import hangman


print("***********************")
print("***Choose your game!***")
print("***********************")

print("(1) Hangman (2) Guessing")

game = int(input("What game?"))

if(game == 1):
  print("Playing hangman")
  hangman.play()
elif(game == 2):
  print("Playing guessing")
  guessing.play()

print("End of the game")