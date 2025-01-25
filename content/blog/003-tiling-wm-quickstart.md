+++
title = 'Tiling WM Quickstart'
date = 2023-08-05T19:53:41+05:00
Categories = ["Computers", "Linux"]
draft = false
+++

I’ve spent about the past year using window managers on-and-off. I have, however, gained an amount of experience with i3 and Qtile. I shall attempt to make getting started with these two WMs a bit easier here.

Please do note that my configuration experience i3 and Qtile is nothing crazy. Everything in this article is just enough to begin getting around these WMs, something I had a bit of trouble with when I started out with this kind of desktop.

Any documentation referenced in this article will be linked below.

# Contents

{{< toc >}}

# i3

Firstly, you’re going to have to install i3. I assume you can do whatever `apt install` or `pacman -S` or `xbps-install` you need to. Just in case, install Xterm too.

Exit your current session and log into your i3 session through your display manager or TTY. You’ll see a prompt asking you to generate a configuration. Press enter here. Then it’ll ask you which key you want as your modifier key. I would suggest choosing the \<Win> option (it maps the modifier key to your keyboard’s windows/command/meta/super key). If you’re particularly crazy, choose \<Alt>.

From this point, you’re going to have a black screen. The most important thing you need to access right now is your terminal. The default keybinding for that is your modifier key + enter.

The configuration is probably located in ~/.config/i3/ 

## Getting function keys to work

Bu default, your brightness, volume and media keys are not going to work.

### Brightness keys

Install a utility called `brightnessctl`. Test if its working in the terminal by executing a command like `brightnessctl set 10%-`. IF you don’t get a permissions error then you’re good to go. Otherwise, add your user to the video group as such: `usermod -aG video $USER`.

Next, let’s bind the appropriate keys.

{{< highlight toml "linenos=inline, style=arduino" >}}
bindsym XF86MonBrightnessUp exec brightnessctl set +1
bindsym XF86MonBrightnessDown exec brightnessctl set 1-
{{< /highlight >}}

You can change the increment amount by changing the integer at the end of the respective lines.

### Volume keys

{{< highlight toml "linenos=inline, style=arduino">}}
bindsym XF86AudioRaiseVolume exec pactl set-sink-volume @DEFAULT_SINK@ +2%
bindsym XF86AudioLowerVolume exec pactl set-sink-volume @DEFAULT_SINK@ -2%
bindsym XF86AudioMute exec pactl set-sink-mute @DEFAULT_SINK@ toggle
{{< /highlight >}}

These commands function for pulseaudio, but I'm not aware of pipewire.

### Media keys

Install a utility called playerctl. The basic commands we are going to use here are `playerctl play-pause`, `playerctl next` and `playerctl previous`. 

{{< highlight toml "linenos=inline, style=arduino">}}
bindsym XF86AudioPlay exec playerctl play-pause
bindsym XF86AudioNext exec playerctl next
bindsym XF86AudioPrev exec playerctl previous
{{< /highlight >}}

If you are a user of MPD, then install `mpc`.

{{< highlight toml "linenos=inline, style=arduino">}}
bindsym XF86AudioPlay exec mpc toggle
bindsym XF86AudioNext exec mpc next
bindsym XF86AudioPrev exec mpc prev
{{< /highlight >}}

## Modifier keys

There are 5 modifier keys available. The ones we're probably going to deal with are:
- `mod1` (left alt key)
- `mod4` (meta/super/command/windows key)

## Creating keybindings

The syntax for creating a keybinding is as such: `bindsym [key-combination] exec [action]`. For example, to open Firefox, you would do something like `bindsym $mod+w exec firefox`.

If you want to use the shift or control keys in your keybindings, simply add it to the key combination, i.e. `bindsym $mod+Shift+a exec [action]` or `bindsym $mod+Control+b exec [action]`. 

## i3bar

I have close to zero experience with i3bar. I generally use Polybar here instead.

## Autostart

Simple add a line starting with `exec` followed by the command you want to execute: `exec [action]`.

## Conclusion

You should now have a somewhat functional configuration of i3. However, i3 does come with some pretty strange default keybindings, so I would recommend changing those. The i3 documentation is excellent. Have a go through that for guidance.

# Qtile

Firstly, install Qtile. It’ll probably be available in your distribution’s repositories; if not you can build it from [source](https://docs.qtile.org/en/stable/manual/install/index.html#installing-from-source). Just in case, also install Xterm.

Once you’ve logged into a Qtile session, press windows/command/super/meta + enter to bring up a terminal.

The default configuration file should be located in `~/.config/qtile/`. If it isn’t, `mkdir .config/qtile`, `cd .config/qtile`, `touch config.py`. Copy the default configuration from [here](https://docs.qtile.org/en/stable/manual/config/default.html#default-config) and paste it into `config.py`. 

## Keybindings

Keybindings are defined in the `keys` array towards the top of the file. They follow the syntax `Key([modifier], "key", action)`.

## Function keys

Function keys probably won't work out of the box. Let's configure them.

### Brightness keys

Install `brightnessctl`. Make sure there are no issues with permissions, as detailed above.

{{< highlight python "linenos=inline, style=arduino">}}
Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +1")),
Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 1-")),
{{< /highlight >}}

### Volume keys

{{< highlight python "linenos=inline, style=arduino">}}
Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +2%")),
Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -2%")),
Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
{{< /highlight >}}

### Media keys

Install `playerctl`.

{{< highlight python "linenos=inline, style=arduino">}}
Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
{{< /highlight >}}

If you are a user of MPD,

{{< highlight python "linenos=inline, style=arduino">}}
Key([], "XF86AudioPlay", lazy.spawn("mpc toggle")),
Key([], "XF86AudioNext", lazy.spawn("mpc next")),
Key([], "XF86AudioPrev", lazy.spawn("mpc prev")),
{{< /highlight >}}

## Layouts

Absolutely take the time to go through the [layouts](https://docs.qtile.org/en/stable/manual/ref/layouts.html) in the documentation. Some of these are a bit fiddly, but the ones I found most usable were ‘MonadTall’, ‘MonadWide’ and ‘TreeTab’. Your milage will vary.

## The bar

Qtile has a pretty capable bar. The built-in widgets are [here](https://docs.qtile.org/en/stable/manual/ref/widgets.html).

## Conclusion

You should have a somewhat functional system at this point. I would absolutely recommend checking out the documentation. It is very well written.

# A few more things

You’re probably going to want to set a wallpaper. *Nitrogen* is a good utility for this.

For compositing, *picom* or *xcompmgr*. There are others, but these are the only ones I’ve used.

For tweaking GTK themes, *lxappearance*. QT theming is a bit more of a hassle. Install qt5ct and Kvantum-manager. Simply set the widget style to kvantum in qt5ct.

# Links
- [i3](https://i3wm.org/)
- [i3 documentation](https://i3wm.org/docs/userguide.html)
- [Qtile](https://qtile.org/)
- [Qtile documentation](https://docs.qtile.org/en/stable/index.html)

