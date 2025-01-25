+++
title = 'Patching DWM'
date = 2024-06-20T15:11:11+05:00
Categories = ["Linux", "Computers"]
+++

Patching DWM is incredibly finicky if you choose to use auto-patching programs. Manual patching is the way to go!

I'm going to be applying this patch here: [focusonnetactive](https://dwm.suckless.org/patches/focusonnetactive/).

Let's first acquire the patch itself. I'll save it to a "patches" directory where my DWM source code is located.

The deal with patching manually is being able to read diff files. It's not too difficult, but any formatting is nice to have. I use the *bat* pager (an alternative to *cat*), and this gives me a good idea of what needs to be done.

{{< image 
  frame="true"
  src="img/patching-dwm/patchingdwm1.png"
>}}

The stuff in green is what we need to add. The stuff in red is what we need to remove. The file in which this needs to be done is also specified, in this case, `dwm.c`.

If you look closely, they've specified at which line things need to be added. In the first case, it's around line 514. Go there, then see what matches whatever they've specified.

{{< image 
  frame="true"
  src="img/patching-dwm/patchingdwm2.png"
>}}

It's not an exact match, but we can see the region we need to change is just below it. I've added the new line there.

Rinse and repeat for the rest.

When you're done, simply rebuild your `dwm.c` again. It'll tell you if you have any errors. If you do, they'll likely be minor syntax errors. Read through the output, it's pretty clear.

{{< image 
  frame="true"
  caption="Don't you just love a unisigned integer?"
  src="img/patching-dwm/patchingdwm3.png"
>}}

You might start to get an idea as to why auto-patching programs tend to get really finicky after a while, mostly after you've applied patches. They just insert the code at whatever line is specified in the diff file, which may break syntax or logic, that sort of thing. Auto-patching works fine for the first few patches, but especially on excessively patched DWM configurations, they tend to just not work.

Anyway, that's the first patch I've applied since I went back to DWM. It's been about a month.
