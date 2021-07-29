import tkinter as tk
from random import randint

'''
Bingo MVP
1. Generate 5x5 Bingo Card from 1-90 with unique numbers
2. Button to generate random number 
3. Number on card cancels out if equal to generated number
'''

class BingoCard:
	def __init__(self, root):
		self.chosen_num = 0
		self.card_num = []
		self.rng_num = []
		self.labels = []
		self.minimum = 1
		self.maximum = 90
		self.count_press = 0


	def gen_number(self, stored, lowest, highest):
		#Generate unique number compared to stored list
		random_num = randint(lowest,highest)
		if random_num in stored:
			random_num = BingoCard.gen_number(self, stored, lowest, highest)
		return random_num
	
	def create_card(self):
		#Generate Bingo Card
		bingo = "BINGO"
		for b in range(5):
			self.labels.append(tk.Label(root,text="%s" % bingo[b], width=9, height=5, bg='light blue',font='Times 15 bold'))
			self.labels[b].grid(row=1, column=b %5)
		for i in range(5,30):
			bingo_num = BingoCard.gen_number(self, self.card_num, self.minimum, self.maximum)
			bingo_str = str(bingo_num)
			self.card_num.append(bingo_num)
			if i % 2 == 0:
				self.labels.append(tk.Label(root, width=9, height=5, bg='white', text=bingo_str, font='Times 15'))
				self.labels[i].grid(row=(i+5)//5, column=(i+5)%5)
			else:
				if i == 17:
					bingo_str = 'Free Space'
				self.labels.append(tk.Label(root, width=9, height=5, bg='light gray', text=bingo_str, font='Times 15'))
				self.labels[i].grid(row=(i+5)//5, column=(i+5)%5)
	
	def pick_number(self):
		#RNG chooses a number
		self.count_press += 1
		if self.count_press == 1:
			self.labels[17].config(text='X', font='Times 15 bold', bg='red')
		chosen_display = tk.Label(root, text="    ", font='Times 20 bold')
		chosen_display.grid(row=0, column=2)
		self.chosen_num = BingoCard.gen_number(self, self.rng_num, self.minimum, self.maximum)
		self.rng_num.append(self.chosen_num)
		chosen_display.config(text=str(self.chosen_num))
		if self.chosen_num in self.card_num:
			BingoCard.num_match(self, self.chosen_num, self.card_num)

	def num_match(self, chosen_num, num_list):
		#Replace selected number with X to mark that spot has been chosen
		index = num_list.index(chosen_num) + 5
		self.labels[index].config(text='X', font='Times 15 bold', bg='red')
	
	def check_winning(self):
		check_bingo = False
		for i in self.labels:
			pass

root = tk.Tk()
bingo = BingoCard(root)
bingo.create_card()
button = tk.Button(root, text="Pick a number", command=bingo.pick_number,width=10, height=3).grid(row=0,column=0)
root.mainloop()