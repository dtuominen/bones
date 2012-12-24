# Vagrant configuration

Im configuring a vagrant virtual box to work 100% of the time from scratch
and automating the whole process


## Initialization

* install vagrant and its dependences

        gem install vagrant

* initialise a new box


        # The included link is ubuntu 12.04 box with chef and puppet included
        vagrant box add lucid32 http://files.vagrantup.com/lucid32.box
        vagrant init lucid32
        vagrant up



## Using provided config

I have included a basic Vagrantfile that should be pretty basic to set up.
Simply initialize a new box in a directory of your choice, and setup the 
modify Vagrantfile it creates

Note, all of these commands may be replicated in the Vagrantfile,
but i prefer to initialise and create my box manually, and then modifying
the existing vagrant-generated config, so I would recommend running the
initialization commands provided first



## Managing the box

ssh into the box as the user `vagrant` who i believe has su rights w/o
needing a password
    
        vagrant ssh

## Tearing it down

virtualbox is handy for dealing with removal/reassurance, but to shut er down

        vagrant pause   # puts box into suspend state
        # or
        vagrant halt    # shuts down the box asap
        # finish that shit
        vagrant destroy


now you are back to where you began, i will work on scripts for automating 
the actual system configuration very soon. at this point in time,
the system packages and everything will need to be configured.

## Chef setup

TBD... Going to try to use fabric instead of chef.. chef is super bitchy
and using chef-solo(the free version) it is somewhat difficult to execute
remotely.

possibly the chef solo scripts could be created and run locally, then have all chef commands and recipes sshd from the host into the vagrant box?

sounds like lots of work
