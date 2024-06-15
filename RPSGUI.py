import tkinter as tk
from tkinter import messagebox
import random as rd
Moves=["Rock","Paper","Scissors"]
class RPS:
    def __init__(self):
        self.user =0
        self.comp=0
        self.root=tk.Tk()
        label=tk.Label(self.root,text="Choose your move:",font=('Arial',18))
        label.pack(padx=20, pady=20)
        self.buttonframe=tk.Frame(self.root)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)
        self.btn1=tk.Button(self.buttonframe, text="Rock", font=('Arial',18),command=self.Rock)
        self.btn1.grid(row=0, column=0,sticky=tk.W+tk.E)
        self.btn2=tk.Button(self.buttonframe, text="Paper", font=('Arial',18),command=self.Paper)
        self.btn2.grid(row=0, column=1,sticky=tk.W+tk.E)
        self.btn3=tk.Button(self.buttonframe, text="Scissors", font=('Arial',18),command=self.Scissors)
        self.btn3.grid(row=0, column=2,sticky=tk.W+tk.E)
        self.buttonframe.pack(fill='x')
        self.root.mainloop()
    def update_score(self,result):
        if result == "tie":
            messagebox.showinfo("Result", "It's a tie!")
        elif result == "win":
            self.user += 1
            messagebox.showinfo("Result", "You win!")
        elif result == "lose":
            self.comp += 1
            messagebox.showinfo(title="Result", message="Computer wins!")
        print(f"Scoreboard:\nYou: {self.user} Computer: {self.comp}")
        if not messagebox.askyesno(title="Play Again", message="Do you wish to play again?"):
            self.root.destroy()
    def Rock(self):
        Comp_move= rd.choice(Moves)
        print(f"You: Rock  Computer: {Comp_move}")
        if Comp_move == "Rock":
            print("It's a tie")
            self.update_score("tie")
        elif Comp_move == "Paper":
            print("Computer wins")
            self.update_score("lose")
        elif Comp_move == "Scissors":
            print("You win")
            self.update_score("win")
    def Paper(self):
        Comp_move= rd.choice(Moves)
        print(f"You: Paper  Computer: {Comp_move}")
        if Comp_move == "Rock":
            print("You win")
            self.update_score("win")
        elif Comp_move == "Paper":
            print("It's a tie")
            self.update_score("tie")
        elif Comp_move == "Scissors":
            print("Computer wins")
            self.update_score("lose")
    def Scissors(self):
        Comp_move= rd.choice(Moves)
        print(f"You: Scissors  Computer: {Comp_move}")
        if Comp_move == "Rock":
            print("Computer wins")
            self.update_score("lose")
        elif Comp_move == "Paper":
            print("You win")
            self.update_score("win")
        elif Comp_move == "Scissors":
            print("It's a tie")
            self.update_score("tie")
RPS()