"""
	A book inventory as a desktop app

	Stores the following about books:
	Title
	Year
	Author
	ISBN

	User can do the following:
	View entries
	Search entries
	Add entries
	Update entries
	Delete entries
	Close app
"""

from tkinter import *
import deskapp_back

def main():
	"""Main execution."""
	window = Tk() 
	Window(window)
	window.mainloop()

class Window():

	def __init__(self, window):
		"""Adding widgets to the window"""
		self.window = window
		self.window.wm_title('BookStore')

		self.database = deskapp_back.Database('books.db')

		l1 = Label(self.window, text='Title')
		l1.grid(row=0, column=0)

		l2 = Label(self.window, text='Author')
		l2.grid(row=0, column=2)

		l3 = Label(self.window, text='Year')
		l3.grid(row=1, column=0)

		l4 = Label(self.window, text='ISBN')
		l4.grid(row=1, column=2)

		self.title_text = StringVar()
		self.e1 = Entry(self.window, textvariable=self.title_text)
		self.e1.grid(row=0, column=1)

		self.author_text = StringVar()
		self.e2 = Entry(self.window, textvariable=self.author_text)
		self.e2.grid(row=0, column=3)

		self.year_text = StringVar()
		self.e3 = Entry(self.window, textvariable=self.year_text)
		self.e3.grid(row=1, column=1)

		self.isbn_text = StringVar()
		self.e4 = Entry(self.window, textvariable=self.isbn_text)
		self.e4.grid(row=1, column=3)

		self.list1 = Listbox(self.window, height=6, width=35)
		self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)

		self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

		sb1 = Scrollbar(self.window)
		sb1.grid(row=2, column=2, rowspan=6)

		self.list1.configure(yscrollcommand=sb1)
		sb1.configure(command=self.list1.yview)

		b1 = Button(self.window, text='View All', width=12, command=self.view_command)
		b1.grid(row=2, column=3)

		b2 = Button(self.window, text='Search Entry', width=12, command=self.search_command)
		b2.grid(row=3, column=3)

		b3 = Button(self.window, text='Add Entry', width=12, command=self.add_command)
		b3.grid(row=4, column=3)

		b4 = Button(self.window, text='Update Entry', width=12, command=self.update_command)
		b4.grid(row=5, column=3)

		b5 = Button(self.window, text='Delete Entry', width=12, command=self.delete_command)
		b5.grid(row=6, column=3)

		b1 = Button(self.window, text='Close', width=12, command=self.window.destroy)
		b1.grid(row=7, column=3)

	def view_command(self):
		"""Passes data into the listbox when view button is clicked."""
		self.list1.delete(0, END)
		for row in self.database.view_data():
			self.list1.insert(END, row)

	def search_command(self):
		"""Searched data and passes results into the listbox
		 when search button is clicked."""
		self.list1.delete(0, END)
		for row in self.database.search_data(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):
			self.list1.insert(END, row)

	def add_command(self):
		"""Takes data from user when add button is clicked, 
		and adds that to the database."""
		self.database.insert_data(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
		self.list1.delete(0, END)
		self.list1.insert(END, (self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))

	def get_selected_row(self, event='<<ListboxSelect>>'):
		"""Get the tuple of information of the entry the user clicks on/selects."""
		try:
			index = self.list1.curselection()[0]
			self.selected_tup = self.list1.get(index)

			self.e1.delete(0, END)
			self.e1.insert(END, self.selected_tup[1])

			self.e2.delete(0, END)
			self.e2.insert(END, self.selected_tup[2])

			self.e3.delete(0, END)
			self.e3.insert(END, self.selected_tup[3])

			self.e4.delete(0, END)
			self.e4.insert(END, self.selected_tup[4])
		except IndexError:
			pass

	def delete_command(self):
		"""Delete the entry that the user selected."""
		self.database.delete_data(self.selected_tup[0])

	def update_command(self):
		"""Update the entry that the user selects with the new information."""
		self.database.update_data(self.selected_tup[0], self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())


	

if __name__ == '__main__':
    main()