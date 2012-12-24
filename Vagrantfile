# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant::Config.run do |config|
  config.vm.box = "lucid32"
  config.vm.forward_port 80, 8000
  config.vm.forward_port 8001, 8005
  config.vm.share_folder "projects", "/home/vagrant/proj/", "/home/dylan/proj/"
  config.vm.network :bridged
end
