import kivymd
import webbrowser
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivymd.uix.navigationdrawer import NavigationLayout
from kivymd.icon_definitions import md_icons
from kivymd.toast import toast
from kivymd.uix.imagelist import SmartTileWithLabel
from kivymd.uix.list import OneLineListItem,\
							TwoLineListItem,\
							ThreeLineListItem,\
							OneLineIconListItem,\
							MDList

class TextWaliTile (SmartTileWithLabel):
	pass

class MainNavigator (NavigationLayout):
	pass

class ActivityManager (ScreenManager):
	pass

class HomeActivity (Screen):
	pass

class Scroll (ScrollView):
	pass

class ListView (MDList):
	
	pass

class OneLineIcon(OneLineIconListItem):
	text = '1234567890'
	def on_press(self):
		MyApp().toastit(self.text)
	pass


class MyApp (MDApp):
	def webit (self,link = 'https://www.google.com/'):
		webbrowser.open(link)

	def toastit (self,a='No function yet'):
		toast(a)
		pass

	def build(self):
		
		Builder.load_file('main.kv')
		a = ActivityManager()
		mainNavigator = MainNavigator()
		
		return mainNavigator


if __name__== '__main__':
	MyApp().run()

