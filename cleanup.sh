#!/usr/bin/env bash
cd /home/vagrant/deployment/work/zope/checkout/
ls -A | grep -v .gitkeep | xargs rm -rdf
cd /home/vagrant/deployment/work/roundcube/checkout/
ls -A | grep -v .gitkeep | xargs rm -rdf