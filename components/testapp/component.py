from batou.component import Component
from batou.lib.file import File, Directory

import os


class TestApp(Component):


    def configure(self):

        self.apis_bt_external_login_folder = Directory('apisBtExternalLogin/')
        self += self.apis_bt_external_login_folder

        self.provide('apisBtExternalLogin', self.apis_bt_external_login_folder)

        self += File(os.path.join(self.apis_bt_external_login_folder.path,
                                  'hiddenFrame.php'))
        self += File(os.path.join(self.apis_bt_external_login_folder.path,
                                  'index.php'))
