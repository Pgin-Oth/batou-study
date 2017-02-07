#!/usr/bin/env bash

sudo chgrp -R vagrant /home/vagrant/deployment
sudo chown -R vagrant /home/vagrant/deployment

#cd /home/vagrant/deployment/work/zope/checkout/bliss
#virtualenv bliss
#cd /home/vagrant/deployment/work/roundcube/checkout/roundcube
#virtualenv roundcube