+++
title = 'Void Linux Post-Installation'
date = 2023-08-26T18:14:49+05:00
Categories = ["Linux", "Computers"]
+++

Today, I reinstalled Void Linux. Mostly just to start fresh and get rid of the cruft I had accumulated over the past few months. There are certain things that don't work on my hardware, not specifically with Void, but Linux in general. These are things that need to be fixed.

In case it is of any help, I'm doing this on a late-2012 iMac, since I've found that Macs have unique issues running Linux.

For future reference, and for anyone who may find it useful, this article exists.

# The Kernel

Any kernels above version 6 causes weird issues on my hardware. Such as being unable to adjust the volume of my speakers or change the backlight. Kernel 5.15 works pretty much flawlessly, so that's what I install: `sudo xbps-install linux5.15 linux5.15-headers`.

The kernel headers are important, because without them, other drivers tend not to work. Don't reboot yet. We'll do that at the end.

# WiFi Drivers

I have a BCM4331 WiFi card. This card requires proprietary drivers to function. Thus, we need to install the non-free repository. This grants us access to proprietary software and drivers: `sudo xbps-install void-repo-nonfree`. Then, update the repositories: `sudo xbps-install -Suv`.

Now comes the driver. You can install it as `broadcom-wl-dkms`. I cannot tell you if this works on all Broadcom cards (I expect it doesn't). That's it for Wifi!

# Nvidia Drivers

I have a Nvidia graphics card. Nouveau drivers are usable, I have used that alone for a while, but proprietary drivers tend to yield better performance despite their problems. It is important that you know which version of drivers you need. I happen to need version 390. Thus, I would install it as such: `sudo xbps-install nvidia390 nvidia390-dkms` If you require verson 470, adjust the version as needed.You can see all of the available drivers by querying for them: `xbps-query -Rs nvidia`.

{{<image
  frame="true"
  caption="Available drivers"
  src="img/void-linux-post-install/vl_nv.png"
>}}

# Bluetooth

We've got to install the *bluez* package to get bluetooth working. After that, we need to start the *bluetoothd* and *dbus* services. In my experience, dbus tends to run out-of-the-box, but there's no harm in double checking. Because we're dealing with runit, `sudo ln -s /etc/sv/bluetoothd /var/service` (for bluetoothd); `sudo ln -s /etc/sv/dbus /var/service` (for dbus).

We can deal with connecting bluetooth devices now using either bluetoothctl or blueman (if you're after a graphical bluetooth client). Blueman is fine, and that's what I use mainly, but for pairing devices, I've found bluetoothctl to generally be more reliable.

In a terminal, type `bluetoothctl`. Then, scan on. When you see your device, `trust [address]`. You can tab-complete the address. Then, `pair [address]`. Finally, `connect [address]`.

From this point onwards, blueman works fine. Install it through `sudo xbps-install blueman`.

# Pipewire to Pulseaudio

Pulseaudio works better on my iMac. Thus, I generally install pulseaudio and remove pipewire.

If I connect a bluetooth speaker to this machine now, I'm not able to adjust its volume. It plays at either max volume or zero volume. [This thread](https://unix.stackexchange.com/questions/686200/bluetooth-speaker-volume-control-doesnt-work-but-muting-does-work) on the Unix Stack Exchange has our solution.

Open `/etc/pulse/default.pa`. Change the line `load-module module-bluetooth-discover` to `load-module module-bluetooth-discover avrcp_absolute_volume=false`. This solves our problem. 

{{<image
  frame="true"
  src="img/void-linux-post-install/vl_abs.png"
>}}

# Setting a default kernel

We could do this through the command line, or we could install a package called grub-customizer: `sudo xbps-install grub-customizer`. You'll need root privelages to run it, so if you happen to be running a window manager without a polkit, run it as root from the command line. Go to the "General settings" tab. Under the "default entry" heading, choose what you want. If you want to always boot the same kernel, choose that under "predefined". Otherwise, select "previously booted entry". This will default the kernel to whatever you selected in the previous session. Click save.

{{<image
  frame="true"
  src="img/void-linux-post-install/vl_gc1.png"
>}}

{{<image
  frame="true"
  src="img/void-linux-post-install/vl_gc2.png"
>}}

Now we may reboot. Select the proper kernel, and voila! Everything should work now.

