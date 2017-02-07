#!/usr/bin/env bash
cd /home/vagrant/deployment/work/batou/checkout/batou
ls -A1 | xargs rm -rdf
cd /home/vagrant/deployment/work/zope/checkout/bliss
ls -A1 | xargs rm -rdf
cd /home/vagrant/deployment/work/roundcube/checkout/roundcube
ls -A1 | xargs rm -rdf