+++
title = 'SSH and Android'
date = 2023-08-16T17:50:32+05:00
Categories = ["Computers", "Linux"]
+++

SSH is a pretty nifty tool. I don't have any servers (yet) or anything of the sorts, but it's a neat way for me to access my computer from my phone. It makes transferring files and stuff much easier (easier than KDE Connect at times). For some reason, my SSH setup thing stopped working, so I'm going to fix it. I'll put the intstructions here so that I (and you) can reference it again in the future. This is for connecting to a computer from an Android device.

I'll be using Termius on my (Android) phone.

# Installation

You'll need to install SSH. On Linux, the package generally goes by some variant of the name `openssh`.

If you are a user of *systemd*, you can check if it's working through `sudo systemctl status ssh`. If not, I can only speak for *runit*. On Void Linux, for example, you're going to have to `ln -s /etc/sv/sshd /var/service`. Use root privelages as needed. Then, to enable it, either reboot or run `sv start sshd`. To check its status, `sv status sshd`. This is more of a how-to-use-runit thing, so I'll stop right here.

# The IP Address

The next thing is to get the IP address of what you are going to connect to. This can be found by running `ip address` in your terminal.

This should be enough to now be able to log into your system from your phone. If you're fine with using your computer's password to log in, then this is it.

# Public/Private Keys

The sequence of steps is as follows:

1. Open `/etc/ssh/sshd_config` in a text editor. Change the port number to 2222.
2. On your phone, add your computer as a host (using the IP address we found above along with the new port number).
3. Generate a pair of keys.
4. Export the keys to your computer.

Now, open `/etc/ssh/sshd_config` in a text editor. Search for "PasswordAuthentication". Change the "yes" into a "no".

Now, we should have a working SSH setup.

{{< image
  frame="true"
  caption="Excessive practicality"
  src="img/ssh-android/ssh_src1.png"
>}}
