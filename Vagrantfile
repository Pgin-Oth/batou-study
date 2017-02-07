# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "flyingcircus/nixos-15.09-x86_64"
  config.vm.box_version = ">= 1.2"

  config.vm.network "private_network", ip: "192.168.50.4"
  config.vm.hostname = "default"
  config.vm.synced_folder "shared/bliss_checkout/", "/home/vagrant/deployment/work/zope/checkout/bliss", group: "vagrant", owner: "vagrant"
  config.vm.synced_folder "shared/roundcube_checkout/", "/home/vagrant/deployment/work/roundcube/checkout/roundcube", group: "vagrant", owner: "vagrant"
  config.vm.synced_folder "shared/batou_checkout/", "/home/vagrant/deployment/work/batou/checkout/batou", group: "vagrant", owner: "vagrant"
  config.trigger.after :up do
    info "Create venv in shared folder"
    run_remote "bash /vagrant/prepare.sh"
  end
  config.trigger.before :halt do
    info "Delete file in shared folder."
    run_remote "bash /vagrant/cleanup.sh"
  end
  config.trigger.before :destroy do
    info "Delete file in shared folder."
    run_remote "bash /vagrant/cleanup.sh"
  end
end