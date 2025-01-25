+++
title = 'Setting up Obsidian with Syncthing'
date = 2024-07-07T16:37:04+05:00
Categories = ["Computers"]
+++

I've known of Syncthing for a while but only got around to setting it up a few days ago.

Note that my usage of Obsidian is very simple; nothing more than tasks and a calendar. I've heard of conflict issues with larger note collections, but there is a bit in this article about mitigating that issue. I'm not aware of how well it works for those larger note collections.

# Setting up Syncthing

I'm not going to write another getting started guide for this. There are already plenty. The [official getting started guide](https://docs.syncthing.net/intro/getting-started.html) is great!

# Excluding the .obsidian folder

I definitely do not want this folder to sync. I'm using different themes/configurations on my phone and computer. The official Syncthing documentation has [a bit on ignoring files](https://docs.syncthing.net/users/ignoring.html).

For our purposes, simply create a `.stignore` file. Open that file in a text editor and add ".obsidian". That's it! Do the same on your phone. That'll keep both configurations separate.

# Mitigating conflicts

You're going to have to do this on both devices, but the procedure is the same for both. The only difference is opening the web GUI on the phone. There's a thing for that in the menu.

{{< image 
  frame="true"
  width="50%"
  src="img/syncthing-obsidian/st4.png"
>}}

Now, in the web GUI, go to Actions>Advanced.

{{< image 
  frame="true"
  width="50%"
  src="img/syncthing-obsidian/st1.png"
>}}

From here, select your Obsidian folder from the "folders" tab.

{{< image 
  frame="true"
  src="img/syncthing-obsidian/st2.png"
>}}

Search for an option named "Max Conflicts". Set that value to 0. From my understanding, this option syncs only the version of any file with the latest modification, and should mitigate any potential conflicts.

That's it!


