# Description:
# Plays sound when saving
# Requirements:
# * Sublime Text 2
# * growlnotify (http://growl.info/extras.php), installed in /usr/local/bin/
# Installation:
# 1) Click Tools > New Plugin ...
# 2) Copy/paste this code into the file
# 3) Save the file into the Users directory
import subprocess, sublime, sublime_plugin, os

class GrowlNotifier(sublime_plugin.EventListener):

	def growl(self):
		cmd = 'osascript -e beep'
		subprocess.call(cmd,shell=True)

	def on_post_save(self, view):
		self.growl()