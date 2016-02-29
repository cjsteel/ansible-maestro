# file: git.md

# Using git

a very brief intro

## Install git

        sudo apt-get install git -y

## Configuring git

### ~/.gitconfig

Use ~/.gitconfig to remember your user info so you don't need to type it in each time.

        git config --global user.email "john.doe@gmail.com"
        git config --global user.name "John Doe"
        cat ~/.gitconfig

### ~/.gitignore

Setting in ~/.gitignore tell git to ignore certain files that you **do  not** want to commit to a repository. This could include things like private information, temporary files and so on.

#### Short Ansible example

        # temp files
        *~
        
        # private files
        .private
        .prv
        .vault

#### Many examples

* [A collection of useful .gitignore templates](https://github.com/github/gitignore)

## Working with git

### git add

### git commit

When you are ready to commit 

        git commit -m 'this is my commit message'

### git push

If you own the repository you can push changes directly to it like this:

        git push

##### github configuration

warning: push.default is unset; its implicit value is changing in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the current behavior after the default changes, use:

  git config --global push.default matching

To squelch this message and adopt the new behavior now, use:

  git config --global push.default simple

##### github password

* [Caching your GitHub password in Git](https://help.github.com/articles/caching-your-github-password-in-git/)

###### Cloning via https

* use a credential helper to tell Git to remember your GitHub username and password every time it talks to GitHub.
* credential helper. requires Git 1.7.10+

###### Cloning via ssh

Authenticate using SSH keys (instead of a username and password).


* launch credential helper
* by default it will cache your password for 15 minutes.

Have git use the credential memory cache

        git config --global credential.helper cache


Set the cache to timeout after 1 hour (setting is in seconds).

        git config --global credential.helper 'cache --timeout=3600'

