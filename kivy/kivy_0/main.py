from kivy.app import App

from kivy.uix.button import Button # for works button

from kivy.uix.boxlayout import BoxLayout # display objects vertically
from kivy.uix.gridlayout import GridLayout # for grid style view

from kivy.uix.codeinput import CodeInput # for works code
from kivy.uix.textinput import TextInput # for works text

from pygments.lexers import CLexer # syntax highlighting, support many scripts

from os import system, popen #


class TextEditorApp(App):
# at the end of the class name necessarily NameClassApp def build() <-- start function, owner function

	def add(self, args):
		'''
		open the file(nameF) and read it
		'''
		try:
			with open(self.nameF.text) as file:
				self.code.text = file.read()
		except FileNotFoundError:
			self.check.text = 'Error: file not found!!'




	def compile(self, args, result=''):
		'''create a file to compile it'''
		try:
			with open(self.nameF.text, 'w') as file:
				file.write(self.code.text)
		except FileNotFoundError:
			result = 'Error: file not found!!'
		else:
			system('gcc %s'%(self.nameF.text)) # run compile
			for string in popen('./a.out'): # iterating ower rows
				result += string
		finally:
			self.check.text = result



	def save(self, args):
		''''''
		try:
			with open(self.nameF.text, 'w') as file:
				result = 'Success file saved!'
				file.write(self.code.text)
		except FileNotFoundError:
			result = 'Error: file not found!!'
		finally:
			self.check.text = result



	def build(self):
		root = BoxLayout(orientation='vertical',
		padding=5)# options to display for window
		btn = GridLayout(cols=3,
			size_hint=[1,.07]) #the markup for btn
		self.nameF = TextInput(text='main.c',
			background_color=[1,1,1,1]) # work with derictories
		root.add_widget(self.nameF) # add nameF in app(window)

		btnA = Button(text='Add File',
			on_press=self.add) # what is the function triggered by clicking this button
		btn.add_widget(btnA)

		btnC = Button(text='Compile File',
			on_press=self.compile)
		btn.add_widget(btnC)

		btnS = Button(text='Save File',
			on_press=self.save)
		btn.add_widget(btnS)

		root.add_widget(btn) # add in boxlayout

		self.code = CodeInput(text='',
			lexer=CLexer())
		root.add_widget(self.code) # add codeinput in window

		self.check = TextInput(text='',
			size_hint=[1,.3], background_color=[1,1,1,.3])
		root.add_widget(self.check) # ....

		return root


if __name__ == '__main__':
	TextEditorApp().run()