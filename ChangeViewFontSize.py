import sublime, sublime_plugin

class IncreaseViewFontSizeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		settings = self.view.settings()
		current_view_font_size = settings.get("font_size", 10)
		if current_view_font_size:
			settings.set("font_size", current_view_font_size + 1)

class DecreaseViewFontSizeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		settings = self.view.settings()
		current_view_font_size = settings.get("font_size", 10)
		print(current_view_font_size)
		if current_view_font_size:
			settings.set("font_size", current_view_font_size - 1)