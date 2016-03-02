# pam_common-password.md

## References

* [](http://xmodulo.com/set-password-policy-linux.html)

## Prevent Reusing Old Passwords

**remember=5 prevents the usage of the last five passwords used. The old passwords are stored in **/etc/security/opasswd**

### On Debian, Ubuntu or Linux Mint:

* Look for a line containing **password** and **pam_unix.so**. 

	password	[success=1 default=ignore]	pam_unix.so obscure use_authtok try_first_pass sha512

Edit append **remember=5**: 

	sudo vi /etc/pam.d/common-password

	password     [success=1 default=ignore]    pam_unix.so obscure sha512 remember=5

### On Fedora, CentOS or RHEL:

	sudo vi /etc/pam.d/system-auth

	password   sufficient   pam_unix.so sha512 shadow nullok try_first_pass use_authtok remember=5


## Set Minimum Password Length

This will enforce a password of length (10 - <# of types>), where <# of types> indicates how many different types of characters are used in the password. There are four types (upper-case, lower-case, numeric, and symbol) of characters. So if you use a combination of all four types, and minlen is set to 10, the shorted password allowed would be 6.

* Look the line that contains **password** and **pam_cracklib.so**.
* Append **' minlen=10'**.

### On Debian, Ubuntu or Linux Mint:

	sudo vi /etc/pam.d/common-password

	password   requisite    pam_cracklib.so retry=3 minlen=10 difok=3

## On Fedora, CentOS or RHEL:

	sudo vi /etc/pam.d/system-auth

	password   requisite   pam_cracklib.so retry=3 difok=3 minlen=10


## Set Password Complexity

Look for a line that contains "password" and "pam_cracklib.so", and append "ucredit=-1 lcredit=-2 dcredit=-1 ocredit=-1" to that line. This will force you to include at least one upper-case letter (ucredit), two lower-case letters (lcredit), one digit (dcredit) and one symbol (ocredit).

On Debian, Ubuntu or Linux Mint:
$ sudo vi /etc/pam.d/common-password

password   requisite    pam_cracklib.so retry=3 minlen=10 difok=3 ucredit=-1 lcredit=-2 dcredit=-1 ocredit=-1

On Fedora, CentOS or RHEL:
$ sudo vi /etc/pam.d/system-auth

password   requisite   pam_cracklib.so retry=3 difok=3 minlen=10 ucredit=-1 lcredit=-2 dcredit=-1 ocredit=-1

## Set Password Expiration Period

To set the maximum period of time the current password is valid, edit the following variables in /etc/login.defs.
$ sudo vi /etc/login.defs

PASS_MAX_DAYS   150
PASS_MIN_DAYS   0
PASS_WARN_AGE   7

This will force every user to change their password once every six months, and send out a warning message seven days prior to password expiration.

If you want to set password expiration on per-user basis, use chage command instead. To view password expiration policy for a specific user:
$ sudo chage -l xmodulo

Last password change                                    : Dec 30, 2013
Password expires                                        : never
Password inactive                                       : never
Account expires                                         : never
Minimum number of days between password change          : 0
Maximum number of days between password change          : 99999
Number of days of warning before password expires       : 7

By default, a user's password is set to never expire.

To change the password expiration period for user xmodulo:
$ sudo chage -E 6/30/2014 -m 5 -M 90 -I 30 -W 14 xmodulo

The above command will set the password to expire on 6/30/2014. In addition, the minimum/maximum number of days between password changes is set to 5 and 90 respectively. The account will be locked 30 days after a password expires, and a warning message will be sent out 14 days before password expiration.



