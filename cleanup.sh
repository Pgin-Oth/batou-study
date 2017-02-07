#!/usr/bin/env bash
cd /home/vagrant/deployment/work/batou/checkout/
ls -A1 | xargs rm -rdf
cd /home/vagrant/deployment/work/zope/checkout/
ls -A1 | xargs rm -rdf
cd /home/vagrant/deployment/work/roundcube/checkout/
ls -A1 | xargs rm -rdf
cd /home/vagrant/deployment/work/test/checkout/
ls -A1 | xargs rm -rdf
cd /home/vagrant/deployment/work/test2/checkout/
ls -A1 | xargs rm -rdf
cd /home/vagrant/deployment/work/test3/checkout/
ls -A1 | xargs rm -rdf