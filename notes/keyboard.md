---
btime: 2024-04-12
layout: note.njk
mtime: 2025-01-19
permalink: notes/{{ page.fileSlug }}/index.html
status: scribble
tags:
- developer
title: Keyboard Layout
---
## Challenge 1: Keyboard Layout
The [Swiss German Layout](http://kbdlayout.info/KBDSG/) offers accessible Umlauts.
The [US Layout](http://kbdlayout.info/kbdus) is more practical for coding.

## Challenge 2: OS  and Apple being Apple
Apple has its custom Swiss GermanKeyboard Layout, which places some important special characters such as `[]` or `<>` in different positions than the other OS.
Apple and Windows have their "Command" respectively "Control" key behaving differently.

## Result
I used to switch in between keyboard layouts. US for coding, Swiss German for texting. With the switching of OS I constantly applied the wrong keystrokes for the OS-Layout combo I was operating in.

## Goals
- Any machine I operate with reacts identically to my keyboard inputs.
- Special characters commonly used in programming language are easially accessible (`[]`, `<>`, `{}` ...)
- Language specific characters are easily accessible, too. (äöü, éèà)

## Partial Solutions

### Hardware
The [ZSA Voyager](https://www.zsa.io/voyager) uses an open-source firmware [QMK](https://github.com/zsa/qmk_firmware) for its configuration. This firmware allows us to customize the keyboard layout. Once we’ve designed the layout, we can compile and flash it onto our keyboard. This process writes our custom configuration directly into the keyboard’s onboard memory, meaning the custom layout is recognized and fully functional on any computer the keyboard is connected to, without the need for additional software or drivers.
The keystrokes are interpreted identically as long as we have an identical input source set on the OS (in my case Swiss German).

With this adaptability, we can resolve Challenge 1.

### OS
This could be tackled in different ways. In my situation, I opted for adjusting the Mac because:
- Apple has its unique setup, whilst the rest seems somewhat aligned.
- I feel more comfortable tweaking my machine than the one at work.

#### Create a Windows-like Swiss German Layout
[Ukelele](https://software.sil.org/ukelele/) helps us adjust Keyboard layouts to our needs. Whilst doing that, I took the liberty of removing the dead key behaviour (wait for the next keystroke and potentially modify that character) for keys such as `~`.
Store the file in `~/Library/Keyboard Layouts/` and restart the machine. The new layout should be available in the Keyboard settings.

> todo: upload .keylayout file

#### Swap Command and Control
When I connect the Voyager, I want to swap command and control on my Mac. When using the Laptop keyboard, I actually preferred the OS default.
[Karabiner](https://karabiner-elements.pqrs.org/) allows such modification dependent on the input source.

## Gimmick: Bind Hyper to long F press for the integrated keyboard

Add your own rule to the Complex Modifications of Karabiner:
```json
{
    "description": "Bind hyper to long key hold of F on integrated laptop keyboard",
    "manipulators": [
        {
            "conditions": [
                {
                    "identifiers": [
                        {
                            "is_built_in_keyboard": true
                        }
                    ],
                    "type": "device_if"
                }
            ],
            "from": {
                "key_code": "f",
                "modifiers": {
                    "optional": [
                        "any"
                    ]
                }
            },
            "parameters": {
                "basic.to_if_held_down_threshold_milliseconds": 350
            },
            "to_if_alone": [
                {
                    "key_code": "f"
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": "left_control",
                    "modifiers": [
                        "left_shift",
                        "left_option",
                        "left_command"
                    ]
                }
            ],
            "type": "basic"
        }
    ]
}
```