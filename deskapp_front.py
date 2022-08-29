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
	window.mainloop()

def view_command():
	"""Passes data into the listbox when view button is clicked."""
	list1.delete(0, END)
	for row in deskapp_back.view_data():
		list1.insert(END, row)

def search_command():
	"""Searched data and passes results into the listbox
	 when search button is clicked."""
	list1.delete(0, END)
	for row in deskapp_back.search_data(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
		list1.insert(END, row)

def add_command():
	"""Takes data from user when add button is clicked, 
	and adds that to the database."""
	deskapp_back.insert_data(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
	list1.delete(0, END)
	list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def get_selected_row(event='<<ListboxSelect>>'):
	"""Get the tuple of information of the entry the user clicks on/selects."""
	try:
		global selected_tup
		index = list1.curselection()[0]
		selected_tup = list1.get(index)

		e1.delete(0, END)
		e1.insert(END, selected_tup[1])

		e2.delete(0, END)
		e2.insert(END, selected_tup[2])

		e3.delete(0, END)
		e3.insert(END, selected_tup[3])

		e4.delete(0, END)
		e4.insert(END, selected_tup[4])
	except IndexError:
		pass

def delete_command():
	"""Delete the entry that the user selected."""
	deskapp_back.delete_data(selected_tup[0])

def update_command():
	"""Update the entry that the user selects with the new information."""
	deskapp_back.update_data(selected_tup[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
	print(selected_tup[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

window = Tk() 

window.wm_title('BookStore')

l1 = Label(window, text='Title')
l1.grid(row=0, column=0)

l2 = Label(window, text='Author')
l2.grid(row=0, column=2)

l3 = Label(window, text='Year')
l3.grid(row=1, column=0)

l4 = Label(window, text='ISBN')
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

list1.bind('<<ListboxSelect>>', get_selected_row)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1)
sb1.configure(command=list1.yview)

b1 = Button(window, text='View All', width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text='Search Entry', width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text='Add Entry', width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text='Update Entry', width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text='Delete Entry', width=12, command=delete_command)
b5.grid(row=6, column=3)

b1 = Button(window, text='Close', width=12, command=window.destroy)
b1.grid(row=7, column=3)

if __name__ == '__main__':
    main()