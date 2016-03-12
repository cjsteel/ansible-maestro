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

