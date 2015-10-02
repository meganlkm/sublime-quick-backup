from os import path
from random import getrandbits
from shutil import copy2
import sublime
import sublime_plugin


class MkFileBackupCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        win_vars = self.view.window().extract_variables()
        newpath = self.get_new_path(win_vars)
        copy2(win_vars['file'], newpath)
        sublime.status_message('backup file saved: {}'.format(newpath))

    def get_new_path(self, window_vars):
        newfilepath = path.join(window_vars['file_path'], self.generate_filename(window_vars))
        while path.exists(newfilepath):
            newfilepath = path.join(window_vars['file_path'], self.generate_filename(window_vars))
        return newfilepath

    def generate_filename(self, window_vars):
        return '{}-backup-{}.{}'.format(window_vars['file_base_name'],
                                        str(getrandbits(32)),
                                        window_vars['file_extension'])
