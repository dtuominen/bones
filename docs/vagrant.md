# Vagrant configuration

Im configuring a vagrant virtual box to work 100% of the time from scratch
and automating the whole process


## Initialization

* install vagrant and its dependences

        gem install vagrant

* initialise a new box


        vagrant box add lucid32 http://files.vagrantup.com/lucid32.box
        vagrant init lucid32
        # Before executing vagrant up, you should modify the Vagrantfile
        # to look like the one provided
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

i need to learn more about vagrant provisioning, which is for this exact purpose

basically vagrant needs to provision chef recipes which exist for setting up and configuring 
packages/anything on the box.

Can't invest too much time in this at the moment, ideally i can automate every single package
or setup task possible, there's a decent resource for chef recipes.
