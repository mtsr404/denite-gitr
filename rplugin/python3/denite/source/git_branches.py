import os.path
import subprocess
from .base import Base


class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'git_branches'
        self.kind = 'git_branch'

        # self.sorters = ['sorter_length', 'sorter_word']
        self.vars = {
                'projectDir': '.'
                }

    def gather_candidates(self, context):
        def create(word ):

            return {
                'word': word,
            }


        command = 'cd {0} && git branch'.format(self.vars['projectDir'])
        response = subprocess.check_output(command, shell=True).decode('utf-8')
        branches = response.split('\n')[1:]

        results = []
        for branch in branches[0:-1]:
            results.extend([create(branch.rstrip())])

        return results
