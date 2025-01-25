+++
title = 'Change your Linux distribution and keep your data!'
date = 2024-05-21T20:27:20+05:00
Categories = ["Linux", "Computers"]
+++

I remember watching an LTT vdeo about Linux when I started out with this operating system. He mentioned how easy it was to change your Linux distribution while keeping all your data. I've since learned how to do that, so I'll be writing about that here.

You can, of course, copy your data to an external drive and restore from there. You can also not do that and keep your data on your internal disk.

The deal is such: you can do this only if you've partitioned your drive a certain way. The configuration I'm familiar with and use is 4 separate partitions, but as far as I know this can work on as few as 2. I'll go over the configuration with 4.

The 4 paritions you'll need are as such:

- **Swap partition**

  Some research is required to fit your own specifications! Suggestions are all over the place, but generally if you have little RAM then about double that should be the size of your swap partition. If you have plenty of RAM, then to my knowledge, perhaps the same amount of swap space or even double.

- **Boot partition**

  You're going to have to do some of your own research to determine if you actually need one. I'm not very familiar with the differences between UEFI and EFI systems, but there's something to do with that.

  If you do need to make one, then this'll be FAT32, about half a gig, and mounted at `/boot/efi`.

- **Root partition** (storage for system files)

  The minimum size I recall seeing for this was about 20 gigs, but I have heard of people having issues with that sort of size. Generally, about 50 gigs should be minimum. The format, if you don't know much about filesystems (like me), is EXT4. Mount this at `/` (the root, as it's called).

- **Home partition** (storage for your own files)

  The bulk of your drive should be taken up by this partition, it's where you'll store all of your files. This is also EXT4, and mounted at `/home`.

Below is a screenshot of how I've set up my hard drive:

{{<image
  src="img/linux-keep-data/data.png"
  frame="true"
  caption="Screenshot for reference!"
>}}

Assuming your disk is set up as such, whenever you change your distribution of Linux, you can do the following: 
- Format your boot partition
- Format your swap partition
- Format your root partition
- ***NOT*** format your home partition

Also! When you set up your new user account, keep the username the same as before! Your data is stored in a folder named after your username in the `/home` partition, so if you choose a different username, your data will still exist, but not accessible to your new user.

I've noticed that deleting most of your dotfiles before doing this tends to help the situation after installing a new image. Keep the ones you know you want, but get rid of the rest. Some things might look weird or act weird on your new installation otherwise.
