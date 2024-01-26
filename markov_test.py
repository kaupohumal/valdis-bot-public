import markovify
import sys

USER = "valdis"
print(f"Selected model name: {USER.upper()}")
print("Creating model...\n")
f = open(f'corpus/{USER}.txt', 'r', encoding="UTF-8")
TEXT_MODEL = markovify.NewlineText(f, state_size=2 ,well_formed = False)
f.close()

while True:
    for i in range(5):
        print(TEXT_MODEL.make_sentence(tries=100))
    input("\nPress ENTER to generate more sentences...\n")


