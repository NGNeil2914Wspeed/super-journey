import tkinter as tk
from tkinter import messagebox
import random as r

player_choice = None
options = ("rock", "paper", "scissors")

# Initialize scores
player_score = 0
computer_score = 0

def start():
    rock_button.config(state="normal")
    paper_button.config(state="normal")
    scissors_button.config(state="normal")
    start_button.config(state="disabled")

def rock():
    global player_choice
    player_choice = "rock"
    computers_choice = r.choice(options)
    end(player_choice, computers_choice)

def paper():
    global player_choice
    player_choice = "paper"
    computers_choice = r.choice(options)
    end(player_choice, computers_choice)

def scissors():
    global player_choice
    player_choice = "scissors"
    computers_choice = r.choice(options)
    end(player_choice, computers_choice)

def end(players_choice, computers_choice):
    global run, player_score, computer_score
    
    if (players_choice == "scissors" and computers_choice == "paper") or \
       (players_choice == "rock" and computers_choice == "scissors") or \
       (players_choice == "paper" and computers_choice == "rock"):
        winner = "player"
        player_score += 1
    elif players_choice == computers_choice:
        winner = "draw"
    else:
        winner = "computer"
        computer_score += 1
        
    # Update the score display immediately
    score_label.config(text=f"Player: {player_score}  |  Computer: {computer_score}")
        
    if winner == "player":
        run = messagebox.askyesno("Result of the round", f"Congratulations! You have won the round as you chose {players_choice} and the computer chose {computers_choice}.\nWould you like to continue playing?")
    elif winner == "computer":
        run = messagebox.askyesno("Result of the round", f"The computer has won the round as you chose {players_choice} and the computer chose {computers_choice}.\nWould you like to continue playing?")
    else:
        run = messagebox.askyesno("Result of the round", f"You have tied the round as you both chose {players_choice}.\nWould you like to continue playing?")
        
    if run:
        rock_button.config(state="disabled")
        paper_button.config(state="disabled")
        scissors_button.config(state="disabled")
        start_button.config(state="normal")
    else:
        root.destroy()

root = tk.Tk()
root.title("Rock paper scissors")
root.geometry("450x450") # Increased height slightly to fit the score safely
root.config(bg="red")

font_title = ("Arial", 20)
font_info = ("Arial", 16)

title = tk.Label(root, text="Rock paper scissors machine", font=font_title, fg="black", bg="red")
title.pack(pady=10)

frame = tk.Frame(root, bg="red")
frame.pack(pady=10)

rock_button = tk.Button(frame, bg="white", text="Rock", fg="black", font=font_info, command=rock)
rock_button.grid(column=0, row=0, pady=20, padx=10)
rock_button.config(state="disabled")

paper_button = tk.Button(frame, bg="white", text="Paper", fg="black", font=font_info, command=paper)
paper_button.grid(column=1, row=0, pady=20, padx=10)
paper_button.config(state="disabled")

scissors_button = tk.Button(frame, bg="white", text="Scissors", fg="black", font=font_info, command=scissors)
scissors_button.grid(column=2, row=0, pady=20, padx=10)
scissors_button.config(state="disabled")

start_button = tk.Button(frame, bg="white", text="Start", fg="black", font=font_info, command=start)
start_button.grid(column=1, row=1, pady=20, padx=10)

# New Score Tracker UI element added at the bottom
score_label = tk.Label(root, text=f"Player: {player_score}  |  Computer: {computer_score}", font=font_info, fg="black", bg="white", width=25, relief="groove")
score_label.pack(side="bottom", pady=20)

root.mainloop()