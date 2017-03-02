from batou.component import Component, platform, Attribute
from batou.lib.file import File
from batou.utils import Address

import socket


def resolve_v6(address):
    try:
        return socket.getaddrinfo(
            address.connect.host,
            address.connect.port,
            socket.AF_INET6)[0][4][0]
    except socket.gaierror:
        return ''


class Nginx(Component):

    """This component configures the Nginx system installation, more
    specifically it configures a specific virtual host.

    It is used by other components below to configure specific virtual
    hosts."""

    public_name = None
    alias = ''
    config_filename = ''
    additional_config = {}
    ssl_on = Attribute(bool, True)
    ssl_key = None
    ssl_cert = None
    fastcgi_params_path = '/etc/nginx/fastcgi_params'

    def configure(self):
        self.address = Address(self.public_name, 80)
        self.address.listen.host_v6 = resolve_v6(self.address)
        self.ssl_address = Address(self.public_name, 443)
        self.ssl_address.listen.host_v6 = resolve_v6(self.ssl_address)
        if self.config_filename:
            self += File('/etc/nginx/local/{}.conf'.format(self.public_name),
                         source=self.config_filename)
        else:
            self += File('/etc/nginx/local/{}.conf'.format(self.public_name),
                         source='{}.conf'.format(self.public_name))


class NginxMail(Component):

    public_name = 'mail.apis.de'
    config_filename = 'mail.apis.de.conf'
    alias = 'www.mail.apis.de'
    letsencrypt = ''
    use_tls = Attribute('literal', False)
    nginx = ''

    def configure(self):
        self.provide('nginxmail', self)
        #self.letsencrypt = self.require_one('letsencrypt')
        #self.nginx = Nginx(public_name=self.public_name,
        #              alias=self.alias,
        #              config_filename=self.config_filename,
        #              # letsencrypt=self.letsencrypt,
        #              use_tls=self.use_tls)
        #self += self.nginx


@platform('gocept.net', Nginx)
class NginxFC(Component):

    cmd_str = 'sudo /etc/init.d/nginx reload'

    def verify(self):
        self.parent.assert_no_subcomponent_changes()

    def update(self):
        self.cmd(self.cmd_str)


@platform('debian', Nginx)
class NginxDebian(Component):

    cmd_str = 'sudo /etc/init.d/nginx reload'

    def verify(self):
        self.parent.assert_no_subcomponent_changes()

    def update(self):
        self.cmd(self.cmd_str)


@platform('vagrant', Nginx)
class VagrantNixOSRebuild(Component):

    cmd_str = 'sudo nixos-rebuild switch'

    def verify(self):
        self.parent.assert_no_subcomponent_changes()

    def update(self):
        self.cmd(self.cmd_str)


@platform('local0', Nginx)
class NginxLocal(Component):

    cmd_str = 'echo NginxLocal0'

    def verify(self):
        self.parent.assert_no_subcomponent_changes()

    def update(self):
        self.cmd(self.cmd_str)


@platform('local1', Nginx)
class NginxLocal(Component):

    cmd_str = 'echo NginxLocal1'

    def verify(self):
        self.parent.assert_no_subcomponent_changes()

    def update(self):
        self.cmd(self.cmd_str)


@platform('local2', Nginx)
class NginxLocal(Component):

    cmd_str = 'echo NginxLocal2'

    def verify(self):
        self.parent.assert_no_subcomponent_changes()

    def update(self):
        self.cmd(self.cmd_str)
