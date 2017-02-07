from batou.component import Component
from batou.lib.file import Directory
from batou.lib.git import Clone

class Zope(Component):

    # https://github.com/Pgin-Oth/batou-study.git

    def configure(self):
        self += Clone('https://github.com/Pgin-Oth/batou-study.git',
                      revision='24761383414e2db213f307bc5eec8ad34792c5f6',
                      target='checkout/bliss/')