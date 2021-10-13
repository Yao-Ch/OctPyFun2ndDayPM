french=("Mer","Ville","Voiture","Ciel","Couleur")
english=("Sea","Town","Car","Sky","Color")

fr_en=dict(zip(french, english))

# or more directly:
    
# fr_en={"Mer":"Sea","Ville":"Town","Voiture":"Car",
#        "Ciel":"Sky",
#        "Couleur":"Color"}

while True:
    answerOrg=input("Enter a french word (or 'Stop'): ")
    answer=answerOrg.lower().capitalize()
    
    if answer == "Stop":
        print("Bye!")
        break 
    if answer in fr_en:
        print(f"Translation of {answerOrg} is {fr_en[answer]}")
    else:
        print(f"No entry for the word: {answerOrg} in my dict")
        print("But I can translate:")
        for fr in sorted(fr_en.keys()):
            print(fr,end=" ")
        print() # to print an empty line
