# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant::Config.run do |config|
  config.vm.box = "lucid32"
  config.vm.forward_port 80, 8000
  config.vm.forward_port 8001, 8005
  config.vm.share_folder "projects", "/home/vagrant/proj/", "/home/dylan/proj/"
  # share folder args are:
  # name of the shared mount on the vagrant vm
  # path to mount the share too on the vm
  # path on host machine
  config.vm.network :bridged
end
