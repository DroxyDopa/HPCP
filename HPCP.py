import random
import time
import tkinter
from tkinter import *
from PIL import Image, ImageTk, ImageSequence

#Loading scene

print(' Welcome to our game :--   Harry Potter and the Chamber of Python')
print('Game loading...(10%)')

seconds = random.randrange(2 , 3)
time.sleep(seconds)
print("Game loading...(25%)")

seconds0 = random.randrange(3 , 4)
time.sleep(seconds0)
print("Game loading...(50%)")

seconds5 = random.randrange(2 , 3)
time.sleep(seconds5)
print("Game loading...(70%)")

seconds1 = random.randrange(3 , 4)
time.sleep(seconds1)
print("Game loading...(98%)")

seconds2 = random.randrange(1 , 2)
time.sleep(seconds2)
print("Game loading...(99%)")

seconds3 = random.randrange(1 , 2)
time.sleep(seconds3)
print("Game loading...(100%)")

seconds4 = random.randrange(1 , 2)
time.sleep(seconds4)
print("Enjoy the Game :-)")


#intro pic
def main(  ):

    filename = "intro pic.png"

    image = Image.open(  filename );
    image.show();

    del image;

if ( __name__  == "__main__" ):

    main();


#intro gif

class App:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = tkinter.Canvas(parent, width=400, height=400)
        self.canvas.pack()
        self.sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                                    Image.open(
                                    r'Sirius.gif'))]
        self.image = self.canvas.create_image(200,200, image=self.sequence[0])
        self.animate(1)
    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        self.parent.after(50, lambda: self.animate((counter+1) % len(self.sequence)))

root = tkinter.Tk()
app = App(root)
root.mainloop()



#quiz
quizpoints=0
q1="""1)What were the first words of Snape told Harry parting his condolences of Lily's Death?
A)Potter, where would you look if I told you to find me a bezoar?
B)Potter! What would I get if I added powdered root of asphodel to an infusion of wormwood?
C)What is the difference, Potter, between monkshood and wolfsbane?
D)Tell me, Potter, what is the color of amortentia?
"""
q2="""2)Who was the student behind the petrified students in ,"Harry Potter And The Chamber Of Secrets"?
A)Justin Finch Fletchley
B)Cho Chang
C)Ginevra Weasley
D)Hermione Granger
"""
q3="""3)Who is Snuffles?
A)James Potter
B)Sirius Black
C)Minerva Mcgonagall
D)Augusta Longbottom
"""
q4="""4)Who helped Harry with the 'GILLYWEED' in the second task of the Triwizard Tournament?
A)Dobby
B)Hermione Granger
C)Neville Longbottom
D)Alastor Moody
"""
q5="""5)To whom was the prophecy made by Proffesor Sybill?
A)Albus Dumbledore
B)Frank Longbottom
C)Severus Snape
D)Lily Potter
"""
q6="""6)Who was the Half blood prince?
A)Severus Snape
B)Draco Malfoy
C)Horace Slughorn
D)Blaise Zabini
"""
q7="""7)Who is Winky?
A)House Elf of The Noble and Most Ancient House of Black
B)Sister of Dobby
C)Ron Weasley's Owl
D)House Elf of the Crouch Family
"""
q8="""8)Which Goblin helps the Golden Trio to get into the Gringotts?
A)Gornuk
B)Gnarlak
C)Griphook
D)Gringott
"""
q9='''9)Who started the Fiendfyre in the Room of Hidden Things?
A)Gregory Goyle
B)Draco Malfoy
C)Blaise Zabini
D)Vincent Crabbe
'''
q10='''10)Who is Teddy?
A)Son of Minerva Mcgonagall and Rubeus Hagrid
B)Son of Nymphadora and Remus Lupin
C)Son of Pansy Parkinson and Luna Lovegood
D)Son of Albus Dumbledore and Dolores Umbridge
'''
q11='''11)How did Myrtle die?
A)She was killed by Olive Hornby after being teased for wearing glasses.
B)She was killed by the Basilisk on Tom Riddle's order.
'''
q12='''12)What question did J.K.Rowling fear the most?
A)What wood was Albus Dumbledore's wand made out of?
B)What were her views on Trans gender?
'''
q13='''13)Which two actors are related to one other in real life?
A)Bill Weasley and Alastor Moody
B)Mundungus Fletcher and Dolores Umbridge
'''
q14='''14)Which three slytherins went after the golden trio to the ROR in the movie?
A)Goyle,Zabini and Malfoy
b)Goyle,Malfoy and Crabbe
'''
q15='''15)Which of this Harry Potter character was based on J.K.Rowling's depression?
A)A Dementor
B)Sirius Black
'''
while quizpoints<15:
    quizpoints=0
    ans1=input(q1)
    while bool(ans1)==True or bool(ans1)==False:
        if ans1 in ('a','b','c','d','A','B','C','D'):
            if ans1=="b"or ans1=="B":
                quizpoints+=1
            break
        else:
            print("That's not an option, Potter.")
            ans1=input(q1)        
    ans2=input(q2)
    while bool(ans2)==True or bool(ans2)==False:
        if ans2 in ('a','b','c','d','A','B','C','D'):
            if ans2=="c"or ans2=="C":
                quizpoints+=1
            break
        else:
            print("That's not an option, Potter.")
            ans2=input(q2)        
    ans3=input(q3)
    while bool(ans3)==True or bool(ans3)==False:
        if ans3 in ('a','b','c','d','A','B','C','D'):
            if ans3=="b"or ans3=="B":
                quizpoints+=1
            break
        else:
            print("That's not an option, Potter.")
            ans3=input(q3)        
    ans4=input(q4)
    while bool(ans4)==True or bool(ans4)==False:
        if ans4 in ('a','b','c','d','A','B','C','D'):
            if ans4=="C"or ans4=="c":
                quizpoints+=1
            break
        else:
            print("That's not an option, Potter.")
            ans4=input(q4)        
    ans5=input(q5)
    while bool(ans5)==True or bool(ans5)==False:
        if ans5 in ('a','b','c','d','A','B','C','D'):
            if ans5=="a"or ans5=="A":
                quizpoints+=1
            break
        else:
            print("That's not an option, Potter.")
            ans5=input(q5)        
    ans6=input(q6)
    while bool(ans6)==True or bool(ans6)==False:
        if ans6 in ('a','b','c','d','A','B','C','D'):
            if ans6=="A"or ans6=="a":
                quizpoints+=1
            break
        else:
            print("That's not an option, Potter.")
            ans6=input(q6)        
    ans7=input(q7)
    while bool(ans7)==True or bool(ans7)==False:
        if ans7 in ('a','b','c','d','A','B','C','D'):
            if ans7=="D"or ans7=="d":
                quizpoints+=1
            break
        else:
            print("That's not an option, Potter.")
            ans7=input(q7)        
    ans8=input(q8)
    while bool(ans8)==True or bool(ans8)==False:
        if ans8 in ('a','b','c','d','A','B','C','D'):
            if ans8=="c"or ans8=="C":
                quizpoints+=1
            break
        else:
            print("That's not an option, Potter.")
            ans8=input(q8)        
    ans9=input(q9)
    while bool(ans9)==True or bool(ans9)==False:
        if ans9 in ('a','b','c','d','A','B','C','D'):
            if ans9=="D"or ans9=="d":
                quizpoints+=1
            break
        else:
            print("That's not an option, Potter.")
            ans9=input(q9)        
    ans10=input(q10)
    while bool(ans10)==True or bool(ans10)==False:
        if ans10 in ('a','b','c','d','A','B','C','D'):
            if ans10=="b"or ans10=="B":
                quizpoints+=1
            break
        else:
            print("That's not an option, Potter.")
            ans10=input(q10)        
    ans11=input(q11)
    while bool(ans11)==True or bool(ans11)==False:
        if ans11 in ('a','b','A','B'):
            if ans11=="b"or ans11=="B":
                quizpoints+=1
            break
        else:
            print("That's not an option, Potter.")
            ans11=input(q11)        
    ans12=input(q12)
    while bool(ans12)==True or bool(ans12)==False:
        if ans12 in ('a','b','A','B'):
            if ans12=="a"or ans12=="A":
                quizpoints+=1
            break
        else:
            print("That's not an option, Potter.")
            ans12=input(q12)    
    ans13=input(q13)
    while bool(ans13)==True or bool(ans13)==False:
        if ans13 in ('a','b','A','B'):
            if ans13=="A"or ans13=="a":
                quizpoints+=1
            break
        else:
            print("That's not an option, Potter.")
            ans13=input(q13)    
    ans14=input(q14)
    while bool(ans14)==True or bool(ans14)==False:
        if ans14 in ('a','b','A','B'):
            if ans14=="a"or ans14=="A":
                quizpoints+=1
            break
        else:
            print("That's not an option, Potter.")
            ans14=input(q14)    
    ans15=input(q15)
    while bool(ans15)==True or bool(ans15)==False:
        if ans15 in ('a','b','A','B'):
            if ans15=="a"or ans15=="A":
                quizpoints+=1
            break
        else:
            print("That's not an option, Potter.")
            ans15=input(q15)    
    if quizpoints>12:
        print("You passed")
        break
    else: print("You didn't get even 10 right, Think harder Potter! You have gotta be smart as a whip to defeat these Death Eaters!")


#D1 pic
def main(  ):


    filename = "D1 pic.png"

    image1 = Image.open(  filename );
    image1.show();

    del image1;

if ( __name__  == "__main__" ):

    main();


#D1 gif    
class App1:
    def __init__(self, parent):
        self.parent1 = parent
        self.canvas1 = tkinter.Canvas(parent, width=500, height=500)
        self.canvas1.pack()
        self.sequence1 = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                                    Image.open(
                                    r'prophecy.gif'))]
        self.image = self.canvas1.create_image(200,200, image=self.sequence1[0])
        self.animate(1)
    def animate(self, counter):
        self.canvas1.itemconfig(self.image, image=self.sequence1[counter])
        self.parent1.after(20, lambda: self.animate((counter+1) % len(self.sequence1)))

root = tkinter.Tk()
app = App1(root)
root.mainloop()


#crossword
print('                                                                  7)\n')
print('                                                                   * \n')
print('                          6)                                      *\n')
print('                           *                                       *           8)\n')
print('                           *                      9)              *           *\n')
print('3)  *    *    *    *     C    *    *     *    A    *    *    O    *     U    *\n')
print('                           *                      *                             *\n')
print('                           *                      *                             *\n')
print('                           *                 4)  *  *  *  *  *\n')
print('         2)  *  *  *  *  S                     *         10)\n')
print('                           *                      *          *\n')
print('                           *                      *          *\n')
print('                           *                      *          *\n')
print('                           *                 5)  A  *  *   I  *\n')
print('       1) *    *    *    A   *   *                         *\n')
print('                                                              *')
print('\n\n Q1-5 are horizontal and Q6-10 are verticle')



time.sleep(1.5)


quizpoints = 0

q1="""1) The Gryffindor who was scared of spiders -- """

q2="""2) 'Nox' is a counter-spell for which spell -- """

q3="""3) Incantation of the charm used against Dementors -- """

q4="""4) Who quoted "There's no need to call me 'Sir', Professor -- """

q5="""5) Incantation of the summoning charm -- """

q6="""6) Incantation of spell which immitates the blow of a sword and leaves deep grooves in the person's body -- """

q7="""7) Who quoted "My father will hear about this!" -- """

q8="""8) The one who could see Nargles -- """

q9="""9) Incantation of spell used to open locked doors -- """

q10="""10) The slytherin whose mother was widowed 7 times -- """



ans1=input(q1)
while bool(ans1)==True or bool(ans1)==False:
    if ans1=="RONALD"or ans1=="ronald"or ans1=="Ronald" or ans1=="Ron" or  ans1=="ron" or ans1=="RON":
        quizpoints+=1
        break
    else: print("Wrong answer!! Think harder, Potter!")
    ans1=input(q1)

ans2=input(q2)
while bool(ans2)==True or bool(ans2)==False:
    if ans2=="LUMOS"or ans2=="Lumos"or ans2=="lumos":
        quizpoints+=1
        break
    else:print("Wrong answer!! Think harder, Potter!")
    ans2=input(q2)
ans3=input(q3)
while bool(ans3)==True or bool(ans3)==False:
    if ans3=="Expecto Patronum"or ans3=="expecto patronum"or ans3=="EXPECTO PATRONUM"or ans3=="Expecto patronum":
        quizpoints+=1
        break
    else:print("Wrong answer!! Think harder, Potter!")
    ans3=input(q3)
ans4=input(q4)
while bool(ans4)==True or bool(ans4)==False:
    if ans4=="harry"or ans4=="HARRY"or ans4=="Harry":
            quizpoints+=1
            break
    else:print("Wrong answer!! Think harder, Potter!")
    ans4=input(q4)        
ans5=input(q5)
while bool(ans5)==True or bool(ans5)==False:
    if ans5=="accio"or ans5=="Accio"or ans5=="ACCIO":
        quizpoints+=1
        break
    else:print("Wrong answer!! Think harder, Potter!")
    ans5=input(q5)        
ans6=input(q6)
while bool(ans6)==True or bool(ans6)==False:
    if ans6=="SECTUMSEMPRA"or ans6=="sectumsempra"or ans6=="Sectumsempra":
            quizpoints+=1
            break
    else:print("Wrong answer!! Think harder, Potter!")
    ans6=input(q6)
ans7=input(q7)
while bool(ans7)==True or bool(ans7)==False:
    if ans7 in ('Draco' , 'DRACO' , 'draco'):
        if ans7=="Draco"or ans7=="draco"or ans7=="DRACO":
            quizpoints+=1
            break
    else:print("Wrong answer!! Think harder, Potter!")
    ans7=input(q7)
ans8=input(q8)
while bool(ans8)==True or bool(ans8)==False:
    if ans8=="Luna"or ans8=="luna"or ans8=="LUNA":
        quizpoints+=1
        break
    else:print("Wrong answer!! Think harder, Potter!")
    ans8=input(q8)        
ans9=input(q9)
while bool(ans9)==True or bool(ans9)==False:
    if ans9=="ALOHOMORA"or ans9=="alohomora"or ans9=="Alohomora":
            quizpoints+=1
            break
    else:print("Wrong answer!! Think harder, Potter!")
    ans9=input(q9)
ans10=input(q10)
while bool(ans10)==True or bool(ans10)==False:
    if ans10=="blaise"or ans10=="Blaise"or ans10=="BLAISE":
        quizpoints+=1
        break
    else:print("Wrong answer!! Think harder, Potter!")
    ans10=input(q10)


if quizpoints>9:
    print("You've Cracked it...Magnificent!!!")
    seconds = random.randrange(4,5)
    time.sleep(seconds)
    print('                                                                       D \n')
    print('                                                                       R\n')
    print('                           S                                          A\n')
    print('                           E                                          C           L\n')
    print('  E    X    P    E    C    T    O     P    A    T    R    O    N    U    M\n')
    print('                           T                        L                             N\n')
    print('                           U                       O                             A\n')
    print('                           M                       H  A  R  R  Y\n')
    print('         L  U  M  O  S                        O\n')
    print('                           E                        M          B\n')
    print('                           M                       O           L\n')
    print('                           P                        R          A\n')
    print('                           R                        A  C  C  I  O\n')
    print('        R    O    N    A   L   D                          S\n')
    print('                                                                  E')




#D2 pic
def main(  ):


    filename = "D2 pic.png"

    image2 = Image.open(  filename );
    image2.show();

    del image2;

if ( __name__  == "__main__" ):

    main();



#D2 gif
class App2:
    def __init__(self, parent):
        self.parent2 = parent
        self.canvas2 = tkinter.Canvas(parent, width=400, height=400)
        self.canvas2.pack()
        self.sequence2 = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                                    Image.open(
                                    r'battle.gif'))]
        self.image = self.canvas2.create_image(200,200, image=self.sequence2[0])
        self.animate(1)
    def animate(self, counter):
        self.canvas2.itemconfig(self.image, image=self.sequence2[counter])
        self.parent2.after(20, lambda: self.animate((counter+1) % len(self.sequence2)))

root = tkinter.Tk()
app = App2(root)
root.mainloop()



#spell battle



e='Expelliarmis'
s='Stupefy'
f='Flipendo'
pm='Protego Maxima'
o='Obscuro'
i = 'Impervius'
c = 'Crucio'
h = 100


print(" Press 1 to cast 'Expelliarmus'\n Press 2 to cast 'Stupefy'\n Press 3 to cast 'Flipendo'\n Press 4 to cast 'Protego Maxima'\n Press 5 to cast 'Obscuro'\n Press 6 to cast 'Impervious'\n Press 7 to cast 'Crucio\n\n Your Health = 100\n Your Points = 10\n\n\n'")


seconds = random.randrange(1,2)
time.sleep(seconds)
ac = print(" Bellatrix casts a spell without any incantation but a fireball is shot at you (Probably it's Lacarnum Inflamari).......What spell do you cast to defend yourself? ")

while True:
    #Take input from the user
    phase1 = input('Enter the number corresponding to the spell you wanna cast')

    #Check if choice is one of the seven options
    if phase1 in ('1','2','3','4','5','6','7'):

        if phase1 == ['4','6']:
            print("You chose to defend like a wise man and retain your health.")
            print("\nYour Health = ",h)
            
        elif phase1 ==['1','2','3','5','7']:
            print("Damn, man you had to defend!... you lost 25% health.")
            h-=25
            print("Your health=",h)
        break

    else:
        print("You were supposed to pick one of the 7 choices. Exploring will get you nowhere!")
        h-=25
        print("Your curiosity cost you your health. It is now",h)

        if h==0:
            def main(  ):

                filename = "D4 pic.png"

                image3 = Image.open(  filename );
                image3.show();

                del image3;

            if ( __name__  == "__main__" ):

                main();


            class App3:
                def __init__(self, parent):
                    self.parent3 = parent
                    self.canvas3 = tkinter.Canvas(parent, width=400, height=400)
                    self.canvas3.pack()
                    self.sequence3 = [ImageTk.PhotoImage(img)
                                      for img in ImageSequence.Iterator(
                                          Image.open(
                                              r'loser.gif'))]
                    self.image = self.canvas3.create_image(200,200, image=self.sequence3[0])
                    self.animate(1)
                def animate(self, counter):
                    self.canvas3.itemconfig(self.image, image=self.sequence3[counter])
                    self.parent3.after(100, lambda: self.animate((counter+1) % len(self.sequence3)))

            root = tkinter.Tk()
            app = App3(root)
            root.mainloop()
            exit()
            print("She casts another Fireball at you. Defend yourself")


if h==0:
    print("You're defeated")

    def main(  ):
        filename = "D4 pic.png"

        image3 = Image.open(  filename );
        image3.show();

        del image3;

    if ( __name__  == "__main__" ):

        main();


    class App3:
        def __init__(self, parent):
            self.parent3 = parent
            self.canvas3 = tkinter.Canvas(parent, width=400, height=400)
            self.canvas3.pack()
            self.sequence3 = [ImageTk.PhotoImage(img)
                              for img in ImageSequence.Iterator(
                                  Image.open(
                                      r'loser.gif'))]
            self.image = self.canvas3.create_image(200,200, image=self.sequence3[0])
            self.animate(1)
        def animate(self, counter):
            self.canvas3.itemconfig(self.image, image=self.sequence3[counter])
            self.parent3.after(100, lambda: self.animate((counter+1) % len(self.sequence3)))

    root = tkinter.Tk()
    app = App3(root)
    root.mainloop()
    exit()
    
patience=0

if h!=100:
    print("Seeing you weak and exhausted, Bellatrix begins mocking you. This is your chance, get her!")
else:
    print("Seeing you nullify her spell, an enraged Bellatrix casts Stupefy at you. Defend yourself !")
while True:
    #Take input from the user
    phase2 = input('Enter the number corresponding to the spell you wanna cast')

    #Check if choice is one of the seven options
    if phase2 in ('1','2','3','4','5','6','7'):

        if phase2 =='4':
            print("You chose to defend like a wise man... you retained your health and gained 20 points")
            print("Your Health = ",h)
            
        elif phase2 =='2':
            print("You both cast the same spell. You hurt her, but she hurt you more.")
            h-=25
            print("Your health=",h)
        elif phase2 =='6':
            print("This was not the spell you should have used here. You get stunned and are knocked unconscious")
            print("\n\n You lost ")

            def main(  ):

                filename = "D4 pic.png"

                image3 = Image.open(  filename );

                image3.show();

                del image3;

            if ( __name__  == "__main__" ):

                main();


                class App3:
                    def __init__(self, parent):
                        self.parent3 = parent
                        self.canvas3 = tkinter.Canvas(parent, width=400, height=400)
                        self.canvas3.pack()
                        self.sequence3 = [ImageTk.PhotoImage(img)
                                          for img in ImageSequence.Iterator(
                                              Image.open(
                                                  r'loser.gif'))]
                        self.image = self.canvas3.create_image(200,200, image=self.sequence3[0])
                        self.animate(1)
                    def animate(self, counter):
                        self.canvas3.itemconfig(self.image, image=self.sequence3[counter])
                        self.parent3.after(100, lambda: self.animate((counter+1) % len(self.sequence3)))

                root = tkinter.Tk()
                app = App3(root)
                root.mainloop()
            exit()

        elif phase2 =='1' or phase2 =='5':
            print("Damn, man you had to defend!... you lost 25% health, but this time you did some damage to Bellatrix too!")
            h-=25
            print("Your Health = ",h)
    
        elif phase2 =='2' or phase2 =='3' or phase2 =='7':
            h-=25
            print("Damn, man you had to defend!... you lost 25% health")
            print("Your Health = ",h)
        break

    else:
        print("You were supposed to pick one of the 7 choices. Exploring will get you nowhere!")
        h-=25
        print("Your curiosity cost you your health. It is now",h)
        if h==0:
            def main(  ):

                filename = "D4 pic.png"

                image3 = Image.open(  filename );
                image3.show();

                del image3;

            if ( __name__  == "__main__" ):

                main();


            class App3:
                def __init__(self, parent):
                    self.parent3 = parent
                    self.canvas3 = tkinter.Canvas(parent, width=400, height=400)
                    self.canvas3.pack()
                    self.sequence3 = [ImageTk.PhotoImage(img)
                                      for img in ImageSequence.Iterator(
                                          Image.open(
                                              r'loser.gif'))]
                    self.image = self.canvas3.create_image(200,200, image=self.sequence3[0])
                    self.animate(1)
                def animate(self, counter):
                    self.canvas3.itemconfig(self.image, image=self.sequence3[counter])
                    self.parent3.after(100, lambda: self.animate((counter+1) % len(self.sequence3)))

            root = tkinter.Tk()
            app = App3(root)
            root.mainloop()
            exit()
            print("She casts another Stupefy at you. Defend yourself")
if h==0:
    print("You're defeated")

    def main(  ):
        filename = "D4 pic.png"

        image3 = Image.open(  filename );
        image3.show();

        del image3;

    if ( __name__  == "__main__" ):

        main();


    class App3:
        def __init__(self, parent):
            self.parent3 = parent
            self.canvas3 = tkinter.Canvas(parent, width=400, height=400)
            self.canvas3.pack()
            self.sequence3 = [ImageTk.PhotoImage(img)
                              for img in ImageSequence.Iterator(
                                  Image.open(
                                      r'loser.gif'))]
            self.image = self.canvas3.create_image(200,200, image=self.sequence3[0])
            self.animate(1)
        def animate(self, counter):
            self.canvas3.itemconfig(self.image, image=self.sequence3[counter])
            self.parent3.after(100, lambda: self.animate((counter+1) % len(self.sequence3)))

    root = tkinter.Tk()
    app = App3(root)
    root.mainloop()
    exit()
    
patience=0

if h!=100:
    print("Seeing you weak and exhausted, Bellatrix begins mocking you. This is your chance, get her!")
else:
    print("Seeing you nullify her spells as if she was a first year student, her morale is broken and she begins thinking. This is your chance, get her!")
while True:
    phase3=input("Enter the number corresponding to the spell you wanna cast.")
        #Check if choice is one of the seven options

    if phase3 in ('1','2','3','4','5','6','7'):

            if phase3 =='1':
                print("Bellatrix is hit with Expelliarmus and she's disarmed. You get away from there.")

                def main(  ):

                    filename = "D3 pic.png"

                    image3 = Image.open(  filename );
                    image3.show();

                    del image3;

                if ( __name__  == "__main__" ):

                    main();


                class App3:
                    def __init__(self, parent):
                        self.parent3 = parent
                        self.canvas3 = tkinter.Canvas(parent, width=400, height=400)
                        self.canvas3.pack()
                        self.sequence3 = [ImageTk.PhotoImage(img)
                                          for img in ImageSequence.Iterator(
                                              Image.open(
                                                  r'you did it.gif'))]
                        self.image = self.canvas3.create_image(200,200, image=self.sequence3[0])
                        self.animate(1)
                    def animate(self, counter):
                        self.canvas3.itemconfig(self.image, image=self.sequence3[counter])
                        self.parent3.after(100, lambda: self.animate((counter+1) % len(self.sequence3)))

                root = tkinter.Tk()
                app = App3(root)
                root.mainloop()

            
            elif phase3 =="2":
                print("Bellatrix gets stunned and falls unconscious. You get away from there.")

                def main(  ):

                    filename = "D3 pic.png"

                    image3 = Image.open(  filename );
                    image3.show();

                    del image3;

                if ( __name__  == "__main__" ):

                    main();


                class App3:
                    def __init__(self, parent):
                        self.parent3 = parent
                        self.canvas3 = tkinter.Canvas(parent, width=400, height=400)
                        self.canvas3.pack()
                        self.sequence3 = [ImageTk.PhotoImage(img)
                                          for img in ImageSequence.Iterator(
                                              Image.open(
                                                  r'you did it.gif'))]
                        self.image = self.canvas3.create_image(200,200, image=self.sequence3[0])
                        self.animate(1)
                    def animate(self, counter):
                        self.canvas3.itemconfig(self.image, image=self.sequence3[counter])
                        self.parent3.after(100, lambda: self.animate((counter+1) % len(self.sequence3)))

                root = tkinter.Tk()
                app = App3(root)
                root.mainloop()

            
            elif phase3 =='3':
                print("Bellatrix is knocked out and falls unconscious. You get away from there.")

                def main(  ):

                    filename = "D3 pic.png"

                    image3 = Image.open(  filename );
                    image3.show();

                    del image3;

                if ( __name__  == "__main__" ):

                    main();


                class App3:
                    def __init__(self, parent):
                        self.parent3 = parent
                        self.canvas3 = tkinter.Canvas(parent, width=400, height=400)
                        self.canvas3.pack()
                        self.sequence3 = [ImageTk.PhotoImage(img)
                                          for img in ImageSequence.Iterator(
                                              Image.open(
                                                  r'you did it.gif'))]
                        self.image = self.canvas3.create_image(200,200, image=self.sequence3[0])
                        self.animate(1)
                    def animate(self, counter):
                        self.canvas3.itemconfig(self.image, image=self.sequence3[counter])
                        self.parent3.after(100, lambda: self.animate((counter+1) % len(self.sequence3)))

                root = tkinter.Tk()
                app = App3(root)
                root.mainloop()

            
            elif phase3 =='4':
                print("That was useless because Bellatrix wasn't attacking. She casts 'Bombarda' and the rock beside you explodes and hits you. You are knocked unconscious.")
                print("\nYou're defeated ")

                def main(  ):

                    filename = "D4 pic.png"

                    image3 = Image.open(  filename );
                    image3.show();

                    del image3;

                if ( __name__  == "__main__" ):

                    main();


                class App3:
                    def __init__(self, parent):
                        self.parent3 = parent
                        self.canvas3 = tkinter.Canvas(parent, width=400, height=400)
                        self.canvas3.pack()
                        self.sequence3 = [ImageTk.PhotoImage(img)
                                          for img in ImageSequence.Iterator(
                                              Image.open(
                                                  r'loser.gif'))]
                        self.image = self.canvas3.create_image(200,200, image=self.sequence3[0])
                        self.animate(1)
                    def animate(self, counter):
                        self.canvas3.itemconfig(self.image, image=self.sequence3[counter])
                        self.parent3.after(100, lambda: self.animate((counter+1) % len(self.sequence3)))

                root = tkinter.Tk()
                app = App3(root)
                root.mainloop()

                    
            elif phase3 =='5':
                print("That was useless because Bellatrix wasen't attacking. She casts 'Bombarda' and the rock beside you explodes and hits you. You are knocked unconscious.")
                print("\nYou're defeated ")

                def main(  ):

                    filename = "D4 pic.png"

                    image3 = Image.open(  filename );
                    image3.show();

                    del image3;

                if ( __name__  == "__main__" ):

                    main();


                class App3:
                    def __init__(self, parent):
                        self.parent3 = parent
                        self.canvas3 = tkinter.Canvas(parent, width=400, height=400)
                        self.canvas3.pack()
                        self.sequence3 = [ImageTk.PhotoImage(img)
                                          for img in ImageSequence.Iterator(
                                              Image.open(
                                                  r'loser.gif'))]
                        self.image = self.canvas3.create_image(200,200, image=self.sequence3[0])
                        self.animate(1)
                    def animate(self, counter):
                        self.canvas3.itemconfig(self.image, image=self.sequence3[counter])
                        self.parent3.after(100, lambda: self.animate((counter+1) % len(self.sequence3)))

                root = tkinter.Tk()
                app = App3(root)
                root.mainloop()

                
            elif phase3 =='6':
                print("That was useless because Bellatrix wasen't attacking. She casts 'Bombarda' and the rock beside you explodes and hits you. You are knocked unconscious.")
                print("\nYou're defeated ")

                def main(  ):

                    filename = "D4 pic.png"

                    image3 = Image.open(  filename );
                    image3.show();

                    del image3;

                if ( __name__  == "__main__" ):

                    main();


                class App3:
                    def __init__(self, parent):
                        self.parent3 = parent
                        self.canvas3 = tkinter.Canvas(parent, width=400, height=400)
                        self.canvas3.pack()
                        self.sequence3 = [ImageTk.PhotoImage(img)
                                          for img in ImageSequence.Iterator(
                                              Image.open(
                                                  r'loser.gif'))]
                        self.image = self.canvas3.create_image(200,200, image=self.sequence3[0])
                        self.animate(1)
                    def animate(self, counter):
                        self.canvas3.itemconfig(self.image, image=self.sequence3[counter])
                        self.parent3.after(100, lambda: self.animate((counter+1) % len(self.sequence3)))

                root = tkinter.Tk()
                app = App3(root)
                root.mainloop()

                
            elif phase3 =='7':
                print("Bellatrix cries in immense pain. She is in so much pain that she falls unconscious. You get away from there.")
                print("\nYou won!")

                def main(  ):

                    filename = "D3 pic.png"

                    image3 = Image.open(  filename );
                    image3.show();

                    del image3;

                if ( __name__  == "__main__" ):

                    main();


                class App3:
                    def __init__(self, parent):
                        self.parent3 = parent
                        self.canvas3 = tkinter.Canvas(parent, width=400, height=400)
                        self.canvas3.pack()
                        self.sequence3 = [ImageTk.PhotoImage(img)
                                          for img in ImageSequence.Iterator(
                                              Image.open(
                                                  r'you did it.gif'))]
                        self.image = self.canvas3.create_image(200,200, image=self.sequence3[0])
                        self.animate(1)
                    def animate(self, counter):
                        self.canvas3.itemconfig(self.image, image=self.sequence3[counter])
                        self.parent3.after(100, lambda: self.animate((counter+1) % len(self.sequence3)))

                root = tkinter.Tk()
                app = App3(root)
                root.mainloop()
            break
        
    else:
            patience+=1
            if patience==2:
                print("You took too long and Bellatrix figured she'd just fill you up with pain. She cast the Cruciatus Curse and you fall unconcious due to unbearable pain.")

                def main(  ):
                    filename = "D4 pic.png"

                    image3 = Image.open(  filename );
                    image3.show();

                    del image3;

                if ( __name__  == "__main__" ):

                    main();


                class App3:
                    def __init__(self, parent):
                        self.parent3 = parent
                        self.canvas3 = tkinter.Canvas(parent, width=400, height=400)
                        self.canvas3.pack()
                        self.sequence3 = [ImageTk.PhotoImage(img)
                                          for img in ImageSequence.Iterator(
                                              Image.open(
                                                  r'loser.gif'))]
                        self.image = self.canvas3.create_image(200,200, image=self.sequence3[0])
                        self.animate(1)
                    def animate(self, counter):
                        self.canvas3.itemconfig(self.image, image=self.sequence3[counter])
                        self.parent3.after(100, lambda: self.animate((counter+1) % len(self.sequence3)))

                root = tkinter.Tk()
                app = App3(root)
                root.mainloop()
                break
            else:
                print("Stop messing around and cast something!")