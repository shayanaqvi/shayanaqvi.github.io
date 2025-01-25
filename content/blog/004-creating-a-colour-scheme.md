+++
title = 'Creating a Colour Scheme'
date = 2023-08-08T16:44:18+05:00
Tags = []
Categories = ["Graphics", "Linux", "Computers"]
draft = false
+++

I like this website’s (current) dark mode. So I had a go translating this to a terminal colour scheme. It is somewhat reminiscent of the Solarized colour scheme. Here is a screenshot: 

{{<image
  src="img/cls/cls_terminal.png"
  frame="true"
  caption="Zellij, Helix, Lazygit"
>}}

- Foreground/background:
  - foreground: `#ffe8c1`
  - background: `#132f35`
- Regular colours:
  - black: `#183c44`
  - red: `#da4949`
  - green: `#bcca15`
  - yellow: `#ffb02e`
  - blue: `#35a6e6`
  - magenta: `#d343a2`
  - cyan: `#38c995`
  - white: `#ffe8c1`
- Bright colours:
  - black: `#235662`
  - red: `#ff5757`
  - green: `#ecff14`
  - yellow: `#ffd694`
  - blue: `#4cbfff`
  - magenta: `#ff4cc2`
  - cyan: `#35ffb6`
  - white: `#ffd48f`

I made a few versions of this theme for some of the software I use.

# Helix

Creating a theme for software like this is somewhat difficult since there are many things to theme and you don't know what all of them are. That probably isn't the best approach to this either. So I grabbed the code for a theme from [this repository](https://github.com/CptPotato/helix-themes) and modified the colours and a few other things to make it work for me.

If you want to use this theme, go to Helix's configuration directory. Create a folder named 'themes'. Then, download [this](/files/cls/cls_helix.toml) file. Name it whatever you want.

# Zellij

Open [this](/files/cls/cls_zellij.kdl) file. Copy the contents and paste it into your config.kdl. Change the default theme. 

# Alacritty

Open [this](/files/cls/cls_alacritty.yml) file. Copy the contents and paste it into your config file.
