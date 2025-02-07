+++
title = 'Playstation Vita as a Music Player'
date = 2024-06-08T14:59:59+05:00
Categories = ["Video Games", "Experiments", "Music"]
+++

I'm trying this out, and I haven't committed to it as of yet. There is a lot of jank here if you choose to go down this route. Benefits and drawbacks, all the rest.

There are pretty much 3 options for music playback here. You have the default music player, ElevenMPV-A, and VitaShell. Each have their problems. And there are a fair few of those.

# Default music player

{{< image
  frame="true"
  src="img/vita-music/vm1.png"
>}}

This is probably the most fleshed out music player you're going to get here. It has your standard Artist/Album/Song/Genre support, playlists too, though all things considered, this is quite primitive.

It does have a very pretty interface though.

{{< image
  frame="true"
  src="img/vita-music/vm2.png"
>}}

{{< image
  frame="true"
  src="img/vita-music/vm3.png"
>}}

{{< image
  frame="true"
  src="img/vita-music/vm4.png"
>}}

The default music player (rather obviously) has the best integration with the rest of your Vita. It'll keep playing if you put your device to sleep, and it works with the quick settings menu thing too.


{{< image
  frame="true"
  caption="Quick Menu integration"
  src="img/vita-music/vm5.png"
>}}

{{< image
  frame="true"
  caption="Live Area screen"
  src="img/vita-music/vm6.png"
>}}

I do lament the lack of controls when your device is sleeping. You can't play/pause easily when the thing is in your pocket, for example. You've gotta turn the thing on, unlock, and then play/pause.

I'm not going to complain about the lack of creature comforts you get in modern music players, such as queues and playlist creation and stuff like that. In that sort of regard, you can treat the Vita as an iPod. You've got to manage your library elsewhere.

If you can look past that, the jank here comes from getting your music on to your device. The official way is through Sony's CMA, which (a) isn't supported anymore and (b) does not have a version for Linux. QCMA exists, but in my experience QCMA is also pretty janky. It worked, but it wasn't reliable.

The other way you can import your music library is through a piece of homebrew known as MediaImporter. This works pretty well.

{{< image
  frame="true"
  src="img/vita-music/vm7.png"
>}}

{{< image
  frame="true"
  src="img/vita-music/vm8.png"
>}}

You've got to place your music files in ux0://music. Launch this app, press cross, and it'll add your music to the app, though it doesn't seem to import playlists.

Speaking of playlists, there is an [INCREDIBLY jank workaround](https://yewtu.be/embed/uAMeqs1uhA8?) for them which I found quite funny.

I've not been able to get this app to display album art at all. It's properly embedded in my music files, but it just won't show up.

# VitaShell

More of a file manager than a music player, but it can play your music.

{{< image
  frame="true"
  src="img/vita-music/vm9.png"
>}}

# ElevenMPV-A

This is probably the second best option you've got here, though this has its issues too.

This acts as more of a file browser, which is a definitely a valid way to browse your music, but just not for me.

{{< image
  frame="true"
  src="img/vita-music/vm10.png"
>}}

{{< image
  frame="true"
  src="img/vita-music/vm11.png"
>}}

It does read tags, however, and the player itself is quite similar to the official app. Album art, for me at least, worked only if I had a cover.jpg or cover.png file in the same directory as the rest of the files. Embedded album art didn't seem to show up.

{{< image
  frame="true"
  src="img/vita-music/vm12.png"
>}}

There is integration with the quick settings menu, but play/pause doesn't work. Volume adjustment does, however, so does background playback and all the rest.

# 05/11/2024: How practical is this?

I've used my PS Vita as such on and off since I wrote this article. My conclusion: not worth it.

## Issue #1: Getting music onto the thing

Now, this might be an issue just because I use Linux. I cannot connect the thing to my computer via USB. Then, either the SD card I'm using in the Vita is weirdly formatted OR my Linux installation is borked, since the card isn't recognised whatsoever on my computer.

This leaves me with the world's fastest file transfer method: FTP. How wonderful!

Getting the music recognised by the default player isn't an issue though. The MediaImporter app I mentioned above works great (also for photos and videos).

## Issue #2: Fitting the thing in your pocket

Don't get me wrong: the Vita is pocketable. I have a 1000 model, and it is, by all means, a pocketable device. It can fit in pants with decently tight pockets. It's not a very comfortable way to carry it, and I do worry about the thumbsticks, but you can do it nonetheless.

But as a music player? Consider the fact that the headphone jack is located on the long side of the device.

Now consider how you'll put it in your pocket. That's the problem.

You could put it in a bag or something else, but then you'll come to terms with the next problem.

## Issue #3: No controls while in sleep mode

From what I've read, the PSP had this. You could, for example, press the shoulder buttons to skip tracks. None of this on the Vita. The most you can do is increase/decrease the volume. Otherwise, turn it on, swipe to unlock, then pause/skip. It's a rather odd omission.

