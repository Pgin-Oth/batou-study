# -*- mode: ruby -*-
# vi: set ft=ruby :

def ParseConfigFile(*keys)
    $str = {}
    configFilePath='Components.cfg'
    File.open(configFilePath){ |f|
        f.readlines.each do |i|
            puts i
#           keys.length.times() do |j|
#               if i.include?(keys[j])
#                   get_split_key=i.split("=")
#                   $str[keys[j]] = get_split_key[1].chop
#               end
#           end
        end
    }
end

# ParseConfigFile("a")

Vagrant.configure("2") do |config|
    config.vm.box = "flyingcircus/nixos-15.09-x86_64"
    config.vm.box_version = ">= 1.2"

    config.vm.network "private_network", ip: "192.168.50.4"
    config.vm.hostname = "default"
    File.open('Components.cfg'){ |f|
        f.readlines.each do |component|
            config.vm.synced_folder "shared/#{component.chomp}_checkout/", "/home/vagrant/deployment/work/#{component.chomp}/checkout", group: "vagrant", owner: "vagrant"
        end
    }
    config.trigger.after :up do
        info "Create venv in shared folder"
        run_remote "bash /vagrant/prepare.sh"
    end
    config.trigger.after :destroy do
        info "Delete files in shared folders."
        run "bash cleanup.sh"
    end
end