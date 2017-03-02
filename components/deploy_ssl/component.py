from batou.component import Component, Attribute
from batou.lib.git import Clone
from batou.lib.cron import CronJob
from batou.lib.file import File, Directory


class LetsEncrypt(Component):

    # e.g. ~/.acme.sh
    acme_source_path = Attribute(str, '{{component.workdir}}/.acme.sh')
    # /path/to/webroot. e.g. .well-known is under ~/app/customerupload
    srv_prj_path = Attribute(str, '{{component.workdir}}')
    # web server config path e.g. /etc/nginx/local
    web_server_crt_path = Attribute(str, '/srv/bliss/deployment/work/nginxmail')
    # web server restart command
    web_server_restart_cmd = Attribute(str, 'sudo fc-manage --build')
    script_name = 'ssl_renew.sh'
    public_name = 'mail.apis.de'
    nginxmail = ''

    def last_updated(self):
        pass

    def configure(self):
        self.provide('letsencrypt', self)
        # self.nginxmail = self.require_one('nginxmail')
        # Step 1 Get acme.sh
        # self += Clone('https://github.com/Neilpang/acme.sh.git',
        #               branch='master',
        #               target=self.acme_source_path)
        # Step 2 Prepare Folder and Script
        self += Directory('.well-known/')
        self += Directory('.well-known/acme-challenge/')
        # self += File(self.script_name, mode=0755)
        # Step 3 CronJob {{component.workdir}}/ssl_renew.sh
        # self += CronJob('cd {} && ./{}'.format(self.workdir, self.script_name),
        #                 timing='0 0 * * 0',
        #                 logger='letsencrypt_ssl_renew')


class CmbLetNginx(Component):

    def last_updated(self):
        pass

    def configure(self):
        # self.provide('letsencrypt', self)
        self.letsencrypt = self.require_one('letsencrypt')
        self.nginxmail = self.require_one('nginxmail')
        self.letsencrypt.nginxmail = self.nginxmail
        self.letsencrypt += File(self.letsencrypt.script_name, mode=0755)
