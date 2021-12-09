import tkinter as tk
from tkinter import messagebox
from typing import Text


class Tictactoe:
    def __init__(self, main_frame, player, track_winners_lbl):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.main_frame = main_frame
        self.letter = "X"
        self.btns = list()
        self.player = player
        self.x_wins = 0
        self.o_wins = 0
        self.track_winners_lbl = track_winners_lbl

    def print_board(self):
        self.btns.clear()
        for i in range(3):
            for j in range(3):
                if i == 0:
                    self.btns.append(tk.Button(self.main_frame, text=self.board[i][j], font=("TkFixedFont"), command=lambda m=(i, j): self.add_letter(m)))
                    self.btns[j].grid(row=i, column=j, ipadx=10, ipady=10)
                elif i == 1:
                    self.btns.append(tk.Button(self.main_frame, text=self.board[i][j], font=("TkFixedFont"), command=lambda m=(i,j): self.add_letter(m)))
                    if j == 1:
                        self.btns[i+3].grid(row=i, column=j, ipadx=10, ipady=10, padx=10, pady=10)
                    else: self.btns[j+3].grid(row=i, column=j, ipadx=10, ipady=10)
                elif i == 2:
                    self.btns.append(tk.Button(self.main_frame, text=self.board[i][j], font=("TkFixedFont"), command=lambda m=(i, j): self.add_letter(m)))
                    self.btns[j+6].grid(row=i, column=j, ipadx=10, ipady=10)

    def add_letter(self, m):
        if self.board[m[0]][m[1]] == " ":
            self.board[m[0]][m[1]] = self.letter
        self.print_board()
        if self.check_board():
            return
        self.change_letter()
        self.player.config(text=self.letter)

    def change_letter(self):
        if self.letter == "X":
            self.letter = "O"
        else:
            self.letter = "X"

    def reset_board(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.letter = "X"
        self.player.config(text=self.letter)
        self.print_board()

    def check_board(self):
        d1 = list()
        d2 = list()
        all_spaces = list()
        for i in range(3):
            d1.append(self.board[i][i])
            d2.append(self.board[i][2-i])
            if "".join([self.board[i][j] for j in range(3)]) == "XXX" or "".join([self.board[j][i] for j in range(3)]) == "XXX" or "".join([self.board[i][j] for j in range(3)]) == "OOO" or "".join([self.board[j][i] for j in range(3)]) == "OOO":
                self.show_winner()
                self.reset_board()
                return True
            all_spaces.extend([space for space in self.board[i]])
        if "".join(d1) == "XXX" or "".join(d2) == "XXX" or "".join(d1) == "OOO" or "".join(d2) == "OOO":
            self.show_winner()
            self.reset_board()
            return True
        if " " not in all_spaces:
            self.show_tie()
            self.reset_board()
            return True
    
    def show_winner(self):
        if self.letter == "O":
            self.o_wins += 1
        else: self.x_wins += 1
        self.track_winners_lbl.config(text=f"X won {tic_tac_toe.x_wins} times,    O won {tic_tac_toe.o_wins} times.")
        messagebox.showinfo(title="We have a winner", message=f"The winner is {self.letter}. Congratulations!")
    
    def show_tie(self):
        messagebox.showinfo(title="It's a tie", message="Shocking, nobody won! Try again.")



root = tk.Tk()
root.title("Tic tac toe")

root_frame = tk.Frame(root)
root_frame.grid(row=0, column=0)
root.grid_rowconfigure(0, weight=1)

main_frame = tk.Frame(root_frame)
main_frame.grid(row=0, column=0, padx=30, pady=30)

info_frame = tk.Frame(root_frame)
info_frame.grid(row=0, column=1, sticky="ns", padx=(0,30), pady=(30))
info_frame.grid_rowconfigure(2, weight=1)

player_lbl = tk.Label(info_frame, text="Player:")
player_lbl.grid(row=0, column=0, padx=20)

player = tk.Label(info_frame, text="X", font=("TkFixedFont", 40))
player.grid(row=1, column=0, pady=10)

track_winners_lbl = tk.Label(root, text="This is the first game.")
track_winners_lbl.grid(row=1, column=0, columnspan=2, pady=(0, 5))

tic_tac_toe = Tictactoe(main_frame, player, track_winners_lbl)
tic_tac_toe.print_board()

reset_btn = tk.Button(info_frame, text="Reset board", command=tic_tac_toe.reset_board)
reset_btn.grid(row=2, column=0, sticky="s")

root.mainloop()
