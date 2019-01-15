import sublime, sublime_plugin
import json
import os
from sys import platform


class MyPluginCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		content = self.get_popup_content()
		self.view.show_popup(content, sublime.HTML, location=-1, max_height=500, on_navigate=self.on_choice_textbox)

	def get_popup_content(self):
		resources = sublime.find_resources('popup-window.html')
		content = sublime.load_resource(resources[0])
		return content

	def on_choice_textbox(self, symbol):
		user_styles = os.path.expanduser('~/Library/Application Support/Sublime Text 3/Packages/User/Preferences.sublime-settings')
		styles_data = os.path.expanduser('~/Library/Application Support/Sublime Text 3/Packages/CommentPlagin/styles.json')
		
		with open(user_styles, 'r') as f:
			data_to = json.loads(f.read())

		with open(styles_data, 'r') as f:
			data_from = json.loads(f.read())


		self.change_json(data_from, data_to, symbol, user_styles)


	def change_json(self, data_from, data_to, symbol, user_styles):
		new_style = data_from["styleslist"][int(symbol)]["style"]
		k = int(symbol)
		if k < 5:
			data_to["color_scheme"] = new_style
		else:
			data_to["theme"] = new_style

		with open(user_styles, 'w') as f:
		    f.write(json.dumps(data_to))

		