import os
import random
import sublime, sublime_plugin
from shutil import copy2


class MkFileBackupCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        win_vars = self.view.window().extract_variables()
        newpath = self.generate_filename(win_vars)
        copy2(win_vars['file'], newpath)
        sublime.status_message('backup file saved: {}'.format(newpath))

    def generate_filename(self, window_vars):
        newfilepath = os.path.join(window_vars['file_path'], '{}-backup.{}'.format(window_vars['file_base_name'], window_vars['file_extension']))
        while os.path.exists(newfilepath):
            newname = '{}-backup-{}.{}'.format(window_vars['file_base_name'],
                                               str(random.getrandbits(32)),
                                               window_vars['file_extension'])
            newfilepath = os.path.join(window_vars['file_path'], newname)
        return newfilepath
