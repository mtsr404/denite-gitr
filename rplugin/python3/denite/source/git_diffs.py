import os.path
import subprocess
from .base import Base


class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'git_diffs'
        self.kind = 'git_file'

        # self.sorters = ['sorter_length', 'sorter_word']
        self.vars = {
            'projectDir': '.'
            }

    def gather_candidates(self, context):
        def create(word,diffTarget):

            return {
                'word': word,
                'name': word,
                'diffTarget': diffTarget,
            }


        diffTarget = context['args'][0]
        command = 'cd {0} && git diff --numstat {1}'.format(self.vars['projectDir'], diffTarget)
        response = subprocess.check_output(command, shell=True).decode('utf-8')
        files = response.split('\n')[0:-1]

        results = []
        for fileName in files:
            results.extend([create(fileName.rstrip(),diffTarget)])

        return results
