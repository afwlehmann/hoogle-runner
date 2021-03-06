# Hoogle Runner

Quick and hassle-free access to [Hoogle](http://haskell.org/hoogle) via [krunner](http://userbase.kde.org/Plasma/Krunner).

![Screenshot](https://raw.github.com/afwlehmann/hoogle-runner/master/screenshot.png)

Keep hacking in your favorite IDE, no need to move your fingers off the keyboard and use the mouse.

Simply hit whatever key combo you have configured for [krunner](http://userbase.kde.org/Plasma/Krunner) (defaults to `Alt-F2`) and start your query by typing `hoogle` followed by a space and whatever it is you are looking for, e.g.

```
hoogle (a -> b) -> [a] -> [b]
```

Hit Enter and happily browse the results of your query.

## What does it have that others don't have?

It has its own icon! ;-)

## Installation

### Requirements
- [PyKDE4](http://techbase.kde.org/Development/Languages/Python)

Easily installed, for example, via Ubuntu's package management system like so:

```bash
sudo apt-get install python3-pykde4
```

### Once you have what you need

Clone this repository

```bash
git clone https://github.com/afwlehmann/hoogle-runner.git
```

Then cd into `hoogle-runner` and **either**
- install to your `~/.kde` folder and restart [krunner](http://userbase.kde.org/Plasma/Krunner) manually via

  ```bash
  plasmapkg --type runner -i .
  kquitapp krunner
  sleep 3
  krunner
  ```

**or**

- simply use the provided installer from the archive ;-)

  ```bash
  . install.sh
  ```
