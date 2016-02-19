# maestro

Maestro is an example of a nice way to create and Ansible orchestration system that is ready to start orchestrating. The first system to be configured is the Ansible host itself, sometimes referred to as the **Controller**. 

## Ansible 

Ansible is an opensource agentless system orchestration software created in Python although it supports modules written in many other language. It is relativly new and was recently purchased by Redhat (October 2015)?. It is the second system orchestration system created by the author, Michael Dehaan, the first being Cobbler, a "bare metal" configuration system that configures new systems via PXE.

In addition to the free opensource product Ansible, Ansible also offers a ommercial product called Tower as well as support plans.

Ansible runs on most major operating system (this includes Windows). This script is only concerned with various Linux flavours and OS X at this time.

Products similar to Ansible include:

* Puppet
* fabric

### Code as documentation

One of my favorite things about Ansible scripts is that they are very easy to read and serve as both deployment and orchestration code and documentation making it much easier to add additional enhancements over time.

### References and credits

This document is based on the excellent Udemy course created by Chris Lunsford's called "Mastering Ansible". It is well worth the money and it is the best tutorial I have found on Ansible by far.

* [Latest Releases Via Apt (Ubuntu)](http://docs.ansible.com/ansible/intro_installation.html#latest-releases-via-apt-ubuntu)

## Installing Ansible

Many options exist. The following will give you a stable and easy to maintain up to date version of Ansible. You probably **do not** want the version of Ansible provided in the ubuntu packaging system. It was version 14,x at the time this README was created and will not run this script. Ansible was a great product when it cam out and many improvements have been made and contributed by developers all over the world.

We are going to install from the Ansible created and maintained packages as they will give us the latest version. If you use, for example, the default Ubuntu 12.04 version of Ansible you would end up with version 14.x at the moment and these scripts would not work as you would be missing the ability to use commands like `become` in your script.

        sudo apt-get install software-properties-common
        sudo apt-add-repository ppa:ansible/ansible
        sudo apt-get update
        sudo apt-get install ansible -y

## a git interlude

If you are going to clone this project...

### installing git

     sudo apt-get install git -y

### clone our project


### Configure git

#### ~/.gitconfig

    git config --global user.email "chris.steel@gmail.com"
    git config --global user.name "Christopher Steel"
    cat ~/.gitconfig

#### ~/.gitignore

Edit as required...

#### commit/push

git push

##### github configuration

warning: push.default is unset; its implicit value is changing in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the current behavior after the default changes, use:

  git config --global push.default matching

To squelch this message and adopt the new behavior now, use:

  git config --global push.default simple

##### github password

Caching your GitHub password in Git
https://help.github.com/articles/caching-your-github-password-in-git/


Managing Remotes / Caching your GitHub password in Git
Caching your GitHub password in Git

    mac
    windows
    linux
    all

If you're cloning GitHub repositories using HTTPS, you can use a credential helper to tell Git to remember your GitHub username and password every time it talks to GitHub.

If you clone GitHub repositories using SSH, then you authenticate using SSH keys instead of a username and password. For help setting up an SSH connection, see Generating an SSH Key.

Tip: You need Git 1.7.10 or newer to use the credential helper.

Turn on the credential helper so that Git will save your password in memory for some time. By default, Git will cache your password for 15 minutes.

    On the command line, enter the following:

    git config --global credential.helper cache
    # Set git to use the credential memory cache

    To change the default password cache timeout, enter the following:

    git config --global credential.helper 'cache --timeout=3600'
    # Set the cache to timeout after 1 hour (setting is in seconds)



## Project directory

If you will build the project from scratch.

Create a directory to hold your ansible project or clone this project from GIT AND/OR MERCURIAL URLs HERE


	mkdir ~/maestro
	cd ~/maestro

## Installing maestro project

#### ansible/.gitignore

## Inventory
ee
Our inventory is a list of the hosts for orchestration.In it's most basic form an inventory file is a static list of hostnames or IP addresses but it can be created and used in many other ways.

### Creating our inventory file

In your project root create an inventory directory and file:

        mkdir inventory
        touch inventory/dev

#### Inventory Host Groups

Our inventory list is going to make use of two groups, `workstation` and `maestro`. Any hosts that we want to belong to a group get listed under the group name

        [workstation]
        ws01
        
        [maestro]
        maestro ansible_connection=local

If you where orchestrating webservices instead of `workstation` you might have groups like `loadbalncer`, `webserver`, `proxy`, `mailserver`, `database` and so on.

### Basic inventory test

Using Ansibles default setting our command will not return the current hosts in our inventory file if your project does not contain an `ansible.cfg` file which points to our projects custom inventory location.

    ansible --list-hosts all
    no hosts matched

### Pass an inventory file using -i option

By manually passing our inventory file we are able to get our list of hosts.

        ansible -i inventory/dev --list-hosts all

## ansible.cfg

The default Ansible config file is /etc/ansible/ansible.cfg. We are going to overide parts of it by creating an ansible.cfg in our project directory. More specifically we are going to have it tell Ansible to look for our inventory in `inventory/dev`.

In our project directory we create and then edit our projects `ansible.cfg` file.

        touch ansible.cfg
        nano ansible.cfg

We will add a [defaults] section to our config file and then set the `inventory` variable to our projects local inventory file. Over time you may want to customize `ansible.cfg` even more.

### Contents of `ansible.cfg`

        [defaults]
        inventory = inventory/dev

### Testing our new default inventory location

Once our custom ansible.cfg file is created we can run the following command without passing it the -o option and our inventory file path:

        ansible --list-hosts all

### Using `--list-hosts`

Sometimes you want to target a specific host or group of hosts from your inventory. The `--list-hosts` option can be passed single, multiple or even hosts selected using the `*` wildcard. Here are some examples:

Note: A single `*` must be in quotes to prevent bash from interpreting it.

* Wild card examples

        ansible --list-hosts '*'
        ansible --list-hosts db*

* Using lists of hosts

    * The old way (depreciated) using a colon:
    
        ansible --list-hosts database:webserver

    * The new way using commas:
    
        ansible --list-hosts database,webserver

## Testing our scripts

### /etc/hosts

Edit `/etc/hosts` and add `maestro` as an alias the system controlling  your Ansible orchestration. When finished it should look something like this:

        127.0.0.1	localhost
        127.0.1.1	sam maestro
        
        # The following lines are desirable for IPv6 capable hosts
        ::1     ip6-localhost ip6-loopback
        fe00::0 ip6-localnet
        ff00::0 ip6-mcastprefix
        ff02::1 ip6-allnodes
        ff02::2 ip6-allrouters
        ff02::3 ip6-allhosts

## Gathering information

By default Ansible gathers a number of facts from any target hosts. Here we are going to gather that information and collect if all locally in a directory.

### Resources

* (http://jpmens.net/2012/09/11/watching-ansible-at-work-callbacks/)

### Gathering information on all of the hosts in our inventory.

This is a fast, easy and powerful way to gather all the facts that Ansible gathers from the hosts in your inventory file. Change the local target directory `${HOME}/dump_path` to fit your needs.

        ansible all -m setup --tree ${HOME}/dump_path

#### COnverting to html

        http://json2html.herokuapp.com/

#### Converting html2markdown

    http://www.codefu.org/html2markdown/

## Running our Ansible playbook

Now we will use the `anisble-playbook` command to run our `systems.yml` playbook. In addition we will pass it the `--limit` and `--ask-become-pass`.

Our limit will use the letter `m` followed by the wildcard giving us `--limit=o*`. This will limit our affected hosts to those in our inventory to that start with the letter `m`.

We will also use `--ask-become-pass` to tell ansible-playbook to prompt us for our users sudo password so that we can run commands that require sudo.

        ansible-playbook host.yml --limit=m* --ask-become-pass

### Example output.


## Shorewall

![Shorewall](docs/shorewall.md)
