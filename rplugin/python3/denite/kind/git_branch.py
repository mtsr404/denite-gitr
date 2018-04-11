import urllib.parse

from .file import Kind as File


class Kind(File):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'git_branch'
        self.default_action = 'git_checkout'
        self.vars = {
            'projectDir': '.'
            }

    def action_git_checkout(self, context):
        for target in context['targets']:
            branch = target['word'][2:]

            command = '!cd {0} && git checkout {1} '.format(self.vars['projectDir'],branch)
            self.vim.command(command)

    def action_git_show_diff_files(self, context):
        for target in context['targets']:
            fileName = target['word'].split(' ')[-1]

            command = 'Gdiff {0}'.format(fileName)
            self.vim.command(command)
