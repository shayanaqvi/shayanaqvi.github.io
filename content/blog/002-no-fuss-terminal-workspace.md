+++
title = 'No-Fuss Terminal Workspace'
date = 2023-07-29T19:08:25+05:00
Categories = ["Computers", "Linux"]
draft = false
+++

Working in the terminal is something that I have been steadily warming up to over the past few months. I think its obvious that this kind of workflow isn’t for everyone, but it doesn’t hurt to try it out, does it? Here, I will share a few terminal apps that I found pretty easy to use. 

Table of contents below:

{{< toc >}}

# Text editing

There are many options for text editing in the terminal, and this has become my preferred way of writing notes and writing code. There are, obviously, downsides to this approach, but, generally, I feel like this constitutes a net positive in my books. The gain in speed, especially when you take the time to learn your way around a text editor is amazing. Options are plentiful, but plenty require lots of configuration.

My personal favourite, the one I’ve been using for probably about the last month/month and a half is Helix. And for about half of that time, I used Helix with close to no configuration. Out of the box, Helix is extremely usable. It has pretty sane defaults, and most things come preconfigured in a way that isn’t particularly intrusive. Now, I have made some changes, but I wouldn’t say that any of them are required. It’s mostly just minor tweaks.

The other great thing with Helix is LSP support out-of-the-box. In fact, I would say it’s more trouble installing LSPs than getting them to work.

{{<image
    src="img/terminal-workspace/tw_helix.png"
>}}

The learning curve here is quite steep, a bit less so if you come from Vi/Vim/Neovim. This learning curve is mostly getting the hand of modal text editing (which I will leave to others to explain).

Vim/Neovim are very competent text editors. I’ve never gone all-out on configuring them, nor have I used any preconfigured “distributions” of Neovim for any longer than a few minutes, but these are wonderful pieces of software.

Emacs is a very capable piece of software that can be used for text editing. I spent most of my time in Emacs using the preconfigured Doom Emacs. This comes with vim keybindings out-of-the-box, so text editing is an alright experience. I did try setting up an LSP for Python a few times, and that experience wasn’t great. It was rather slow. But what I liked the most about Emacs was org-mode. It is a much better kind of markup language, and its very capable. It’s problem is that its featureset is pretty much limited to Emacs. But aside from that, Emacs is certainly worth a try.

Right before I jumped on the Vim/Emacs/Helix bandwagon, I spent about 2 days with Micro. Micro is like a better version of GNU Nano. No modal editing, but from what I recall, a better experience than Nano.

All that said, I think for a no-fuss approach to text editing in the terminal, give Helix or Micro a try.

# Terminal Multiplexers

Tmux is an alright piece of software, in my opinion. It takes plenty of configuring to be able to use properly, but once you’ve reached the point where you’re happy with your configuration, it’s plenty usable.

Recently, however, I came across Zellij, and it’s genuinely wonderful! This is another one of those pieces of terminal software that is pretty no-fuss. It has sane defaults, and literally the only change I’ve made to its configuration is its colourscheme. I have changed literally nothing else, because there’s no need. It manages splits in a similar manner to window managers like DWM or Qtile, and a great feature is the ability to have floating windows, in the terminal! It’s a great piece of software, and while it’s not perfect, it gets most of the way.

{{<image
    frame="true"
    caption="Very practical and realistic usage of Zellij"
    src="img/terminal-workspace/tw_zellij.png"
>}}

# Music Players

My experience with terminal music players has mostly been MPD frontends, so I will not talk about non-MPD terminal music players (such as cmus or moc). What I will talk about before touching on MPD frontends is Musikcube. Musikcube is, to my knowledge, a music server (like MPD) and a music player. I used it without paying much heed to its music server feature, and I got plenty far that way. Also, I needed to configure absolutely nothing for it to be usable.

That being said, options are more plentiful on the MPD side of things. One thing to note is that many mpd clients have terrible names. The two I’m most well versed with are ncmpcpp and nncmpp. Both are quite nice, require very, very little configuration (if any), and can get you pretty far. Ncmpcpp is probably the more powerful of the two.

{{<image
    frame="true"
    caption="ncmpcpp"
    src="img/terminal-workspace/tw_ncmpcpp.png"
>}}

Both can be navigated with the keyboard, but mouse support in nncmpp is top tier. Great stuff. 

# File Management

File management is something that can be done purely in the terminal. But using a frontend usually makes things a bit easier.

Options here are plentiful, but I have mostly used ranger and xplr. I’ve only touched others like nnn and lf a few times (though lf is pretty much ranger). 

{{<image
    frame="true"
    caption="xplr"
    src="img/terminal-workspace/tw_xplr.png"
>}}

Again, you can do lots of things here without much configuration, and navigating these apps are plenty fast.

A new file manager I came across is *clifm*. I haven’t used it much, but this is also pretty cool and doesn’t require much configuration.

# Other Apps

Lazygit is pretty nice. Very usable out-of-the-box.

{{<image
    src="img/terminal-workspace/tw_lazygit.png"
>}}

RSS readers such as Newsboat can also go a long way, but this isn’t something I prefer doing in the terminal, I'll get to why below.

# No thanks!

Web browsing in the terminal is a big no-go for me. There are many options (browsh is pretty cool), but all of them, and I mean all of them, are an extremely substandard and subpar experience. This is, obviously, courtesy of the absolute mess that is the modern web. Pure HTML sites are usable, but this is becoming an increasingly rare breed of websites.

Email is something I haven’t got into much myself (I set up alpine and used that a bit for a few weeks). I’ve heard it’s doable and can be a nice experience, but this requires a lot of configuration from what I know. I could, however, very much be wrong.

As I mentioned before, RSS reading. It’s probably the best web-based terminal experience you’re going to get. Reading RSS in the terminal is very much practical, doesn’t require too much configuration, and is quite nice at times. But generally, I feel like I get a better experience here with GUI apps.

# Links
- [Helix](https://helix-editor.com/)
- [Neovim](https://neovim.io/doc/)
- [Vim](https://www.vim.org/)
- [Micro](https://micro-editor.github.io/)
- [GNU Emacs](https://www.gnu.org/software/emacs/)
- [Doom Emacs](https://github.com/doomemacs/doomemacs)
- [Tmux](https://github.com/tmux/tmux/wiki)
- [Zellij](https://zellij.dev/)
- [Musikcube](https://musikcube.com/)
- [ncmpcpp](https://rybczak.net/ncmpcpp/)
- [nncmpp](https://git.janouch.name/p/nncmpp)
- [ranger](https://github.com/ranger/ranger)
- [xplr](https://xplr.dev/)
- [clifm](https://github.com/leo-arch/clifm)
- [Lazygit](https://github.com/jesseduffield/lazygit)
- [Newsboat](https://newsboat.org/index.html)
