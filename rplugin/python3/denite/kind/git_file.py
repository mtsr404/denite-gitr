import urllib.parse

from .file import Kind as File
from .base import Base

class Kind(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'git_file'
        self.default_action = 'git_show_diff_in_file'
        self.vars = {
            'projectDir': '.'
            }


    def action_git_show_diff_in_file(self, context):
        fileName = context['targets'][0]['word'].split()[-1]

        # self.vim.command('Gvdiff master:{0}'.format(fileName))
        # self.vim.command('only')
        self.vim.command('Gina compare \'master:{0}\' '.format(fileName))
        self.vim.command('wincmd k')
        self.vim.command('set foldmethod=diff')
        # self.vim.command('echomsg \'{0}\''.format(fileName))
