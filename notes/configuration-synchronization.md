---
btime: null
layout: note.njk
mtime: 2025-10-19 23:58
permalink: notes/{{ page.fileSlug }}/index.html
status: draft
tags:
- tech/devops
- tech/website/hosted
title: Configuration Synchronization.Md
---
## Configuration Synchronization

I would like to be efficient and "home" on any machine within a few minutes.
Setting up a new computer gets more annoying the more extensive and customized your toolchain is.

In this article I aim to relieve the pain of having to remember (!) and re-install:
- Configurations and preferences that can be stored in text
- Terminal Packages
- GUI applications

Even better, we aim to synchronize those settings across multiple operating systems. In my case I have [WSL](https://ubuntu.com/desktop/wsl) at work and use Mac OS at home. I would like to have similar workflows on both machines.

### Text-Based Configurations
The scope of configurations is limited to program settings, that can be saved in a plain text file. Fortunately this will encompass many developer tools. Those text configurations usually start with a dot in their name (`.zshrc`, `.gitconfig`, `.vimrc` etc.) and are thus commonly named **dotfiles**.
Our goal is to synchronize the dotfiles across multiple machines. You will rightfully be thinking of git. Below, I will introduce a tool that builds on top of it and will eliminate some pain points of tackling the file management with vanilla git.

>[!Note]
Some applications store their settings, history or extensions in a local database. Web browsers are such examples. Those apps often offer a cloud based synchronization through ones user profile.

### Track changes with chezmoi

[chezmoi](https://github.com/twpayne/chezmoi) is our weapon of choice. There are literally [dozens of alternatives](https://dotfiles.github.io/utilities/), though it is the most popular besides plain git. This article is an introduction into its conveniences.

I do aim to give a high level overview and refer to the fantastic [official documentation](https://www.chezmoi.io/) for the details.

#### Track files

Let's start tracking our first dotfile to understand the underlying git flow of chezmoi:
1. `chezmoi init` initializes a local git repo under `~/.local/share/chezmoi`.
2. `chezmoi add .zshrc` starts tracking our `.zshrc` configuration
3. `chezmoi edit .zshrc` edit the configuration
4. `chezmoi apply` apply the changes from the chezmoi git repo to the ones on your system ("source").

![](/assets/images/chezmoi-single-machine.webp)

As the graphic shows, chezmoi mirrors and keeps track of the dotfiles in a git repo at `~/.local/share/chezmoi/`.

If the remote of our dotfiles git repo has changes `chezmoi update` pulls them to our local repo and directly tries to apply them to our corresponding configuration on the machine.

Updating our local changes to the remote is done with regular git commands. `chezmoi cd` directly navigates to it.

#### Machine-specific adjustments
If our `.zshrc` file should look different depending on whether it is on linux or mac, we have to define the dotfile as a template (`.zshrc.tmpl`) within the chezmoi repo. Chezmoi will then render the template onto the target machine.

![](/assets/images/chezmoi-multi-platform.webp)

Within the template, we define the logic of how the file should look different depending on the OS of the source.

```go
# .zshrc.tmpl
{{ if eq .chezmoi.os "darwin" }}
	# On mac homebrew also supports casks
	alias brewup="brew update && brew upgrade && brew upgrade --cask"
{{ else if eq .chezmoi.os "linux" }}
	eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
	alias brewup="brew update && brew upgrade"
{{ end }}
```

On a linux machine, our `.zshrc` will be rendered to

```

eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
alias brewup="brew update && brew upgrade"

```

Note the empty lines 1 and 4. To avoid newlines introduced by the if/end conditionals, we can use a dash in our conditionals: `{{- if ...}` and `{{- end }`.

Useful variables for templating are:
- `.chezmoi.os`: "darwin", "linux", "windows"
- `.chezmoi.hostname`

> [!Tip]
> Chezmoi utilizes Go's text/template package to process template files. If you are looking for more information on how the dashes avoid newlines, check out the [Text and Spaces Section in the Documentation](https://pkg.go.dev/text/template#hdr-Text_and_spaces)

##### Create a template
Let's create our first template.  
My `.zshrc` is already managed by chezmoi, but not yet a template. Let's make it one:

```zsh
chezmoi chattr +template ~/.zshrc
```

When we now use `chezmoi edit ~/.zshrc` we will automatically edit the template.

To preview the template output on the current machine, run

```zsh
chezmoi cd
chezmoi execute-template < dot_zshrc.tmpl
```

If that is how you expect it to look like, don't forget to `chezmoi apply` your changes onto your current machine as well. Without that you have only changed the file within the chezmoi git repo.

>[!Tip] [Official Docs: Templating](https://www.chezmoi.io/user-guide/templating/)

With that we can synchronize files and thus text-based configurations across multiple computers.

### Managing Software
I dislike installing applications and packages through a clicky-clicky download and installer process. Similar to `pip` or `npm` there are system level package managers. We strictly revert to them whenever possible. This includes avoiding to manually update the application through pop-ups of it's user interface. This would potentially get the configuration from the package manager out of sync. Instead, we use the package manager to update it.

#### My package managers of choice
Mac
- [Homebrew](https://brew.sh/): THE package manager on Mac. Can install GUI apps as casks.
Linux / WSL:
- [Homebrew](https://brew.sh/): There would be more alternatives. Choosing it for consistency with my Mac setup. Brew does not support casks on Linux, but I do not need any GUI applications on WSL.
- apt: For initial machine essential installs that I rarely update: (`build-essential`, `curl`, `zsh`). This article will not go into more details regarding that for now.
Windows:
- [scoop](https://scoop.sh/): Not much research went into that one. Admin rights are a bit of a struggle on the work computer, and this seemed to consider that.

#### Specifying required software
It is handy to define the software we'd like to install in a plain yaml configuration file. Unlike our configurations, we do not want to copy this list of packages to our home directory `~/`. Chezmoi treats files within `.chezmoidata` exactly that way. We create our desired package configuration there:

```yaml
#~/.local/share/chezmoi/.chezmoidata/packages.yaml
packages:
  darwin:
    brews:
      - git
      - uv
    casks:
      - firefox
      - obsidian
  linux:
    brews:
      - git
      - uv
      - databricks
  windows:
    scoop:
      - obsidian
      - windirstat
```

Any time changes in that file are detected, we want to pass them to our package manager. On the other hand, if we only updated a dotfile configuration, we do not need and want to interact with the package manager. Chezmoi handily also addresses that need. Script names starting with `run_onchange` are only executed if their content has changed. The script below will run if there are changes of our `packages.yaml`.

```sh
# run_onchange_install-packages.sh.tmpl
{{ if eq .chezmoi.os "darwin" -}}
#!/bin/bash
echo "Installing macOS Homebrew packages and casks ..."
brew bundle --file=/dev/stdin <<EOF
{{range .packages.darwin.brews }}
brew {{ . | quote }}
{{ end -}}
{{ range .packages.darwin.casks -}}
cask {{ . | quote }}
{{ end -}}
EOF
echo "Homebrew bundle for macOS complete."

{{ else if eq .chezmoi.os "linux" -}}
#!/bin/bash
echo "Installing Linux packages..."
brew bundle --file=/dev/stdin <<EOF
{{range .packages.linux.brews }}
brew {{ . | quote }}
{{ end -}}
EOF
echo "Homebrew bundle for Linux complete."
{{ end }}
```

This shell-script will handle installations on Mac and Linux through homebrew. Since no condition is triggered on windows, the file will not be created on a windows machine. Neat. For windows we define a [run_onchange_install-packages.ps1.tmpl](https://github.com/fabitosh/dotfiles/blob/main/run_onchange_install-packages.ps1.tmpl) in similar fashion.

> [!Note]
> [Chezmoi Scripts Guide](https://www.chezmoi.io/user-guide/use-scripts-to-perform-actions/)

With that, we can both manage configurations as well as packages on our machines. You can store and backup the configuration of your entire machine now.

### Setting up a new machine

To install `chezmoi` and directly apply your public github `.dotfiles` repo, we can run

```bash
sh -c "$(curl -fsLS get.chezmoi.io)" -- init --apply github-username.
```

With our configuration so far, this would likely fail though. For example the new machine will not have our package managers installed.
You can decide yourself whether it is worthwhile to automate those steps as well. In general, I am fine with having a few manual steps remaining. To fully control the entire system, [Ansible](https://docs.ansible.com/) and [nix](https://nixos.org/) would be better choices.
### run_once
If we do not want to go through the minor hassle of installing homebrew before applying our dotfiles, scripts starting with`run_once_before` are our friend.

```bash
# ~/.local/share/chezmoi/run_once_before_10-install-homebrew.sh.tmpl
{{ if ne .chezmoi.os "windows" -}} 
#!/bin/sh
# Installs Homebrew if not present, and configures the PATH for this session.

set -e

if ! command -v brew >/dev/null 2>&1; then
  echo "Installing Homebrew..."
  # Run the official installer. This might prompt for the sudo password.
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

else
  echo "Homebrew is already installed."
fi

echo "Homebrew installation script finished."

# --- Configure PATH for the rest of this chezmoi run ---
BREW_PATH=""
if [ -x "/opt/homebrew/bin/brew" ]; then
  # Apple Silicon Macs
  BREW_PATH="/opt/homebrew/bin/brew"
elif [ -x "/usr/local/bin/brew" ]; then
  # Intel Macs
  BREW_PATH="/usr/local/bin/brew"
elif [ -x "/home/linuxbrew/.linuxbrew/bin/brew" ]; then
  # Linux
  BREW_PATH="/home/linuxbrew/.linuxbrew/bin/brew"
fi

if [ -n "$BREW_PATH" ]; then
  eval "$($BREW_PATH shellenv)"
  echo "Homebrew paths have been configured for this session."
fi
# subsequent sessions have their paths defined in the .zshenv
{{ end -}}
```

> [!Tip]
> Further documentation on how to use scripts with chezmoi
> [Use scripts to perform actions](https://www.chezmoi.io/user-guide/use-scripts-to-perform-actions/)
> [Source state attributes](https://www.chezmoi.io/reference/source-state-attributes/)

### Sensitive Information
Do not store any sensitive data in plaintext within the repo. Even if you have the repo private.
- [Encryption is supported](https://www.chezmoi.io/user-guide/encryption/). Have not tested it myself.

### Follow-up Reading
- [fabitosh/dotfiles](https://github.com/fabitosh/dotfiles) My relatively simple dotfiles repo.
- [Managing dotfiles with Chezmoi | Nathaniel Landau](https://natelandau.com/managing-dotfiles-with-chezmoi/): Well explained more advanced setup.
- [#chezmoi on github](https://github.com/search?q=%23chezmoi&type=repositories) Various public dotfiles repos.
- [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/latest/): Keep your home directory clean. Standard on where applications are supposed to store their data.