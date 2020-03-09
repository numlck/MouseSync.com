# ReyonMouseFix
A mousefix that greatly improves aim by quantization (for lack of a better word)
Uses one of the same libraries as Povohat/Kovaaks Mouse Accell | Interaccell 

# What it does

Windows has a mouse calculation that relates to integers. So your mouse can only move whole units like 1,2,3,4
The problem really lies in the fact that Windows doesnt support a decimal number for mouse input like 1.2352 it only supports whole integers like DX = 1,2,3,4 Thereby whatever is considered 1 in real life distance becomes the calibration

ReyonMouseFix directly correlates the mouse distance like (1.2345) into the same screen distance. So i.e 1cm mouse == 1cm screen

or a whole integer thereof like 1:5, you can adjust this in Extra Scale X/Y Setting

# Sidenote 

There is a major bug in the Kovaaks Mouse Accell program namely that they use `floor()` to round the numbers. This works fine for positive decimals but when its negative it finds the lowest number which i.e `-2.326` becomes `-3.0` because `-3.0 < -2.326` but on the positive side it turns `2.326` into `2.0`, and you can test it yourself, your left movement is faster then your right movement.

**This driver doesnt suffer from that.** 

Warning: FaceIT might have problems with the Interception Library contained within this software.

# Experience
- **Diabotical Insane Triple Kill: https://streamable.com/vd4dz**

- **CSGO Test: https://www.youtube.com/watch?v=gvHR4sSql-E**

- **ApexLegends (made by a Top 250 world player) skip to 1:28 : https://streamable.com/bwk0x**





> https://www.reddit.com/r/FPSAimTrainer/comments/f96u6x/github_e9kreyonmousefix_a_mousefix_that_greatly/fipupju?utm_source=share&utm_medium=web2x
>Okay so program seemed safe enough, data being sent out seems non-malicious, so I tried it. Not gonna lie, it might just be placebo, but I definitely feel more consistent and smoother already, though the mouse feel has noticeably changed and I can't tell if there's input lag or whether this is just a result of the quantization.

>Here's a quick clip from bounce 180 that I hit with this driver interceptor. I'd say this is the nicest b180 clip I've ever gotten by a little bit, seems like I can move at quicker speeds without losing as much smoothness and precision. Using GPW @ 37cm/360 on cordura mouse pad. I have the X/Y scaling set to 10 for each, also. 
https://streamable.com/qawug

**Make a pull request if you want to feature your highlight or video in here.**

# How To Install
Download the latest release from https://github.com/e9k/ReyonMouseFix/releases

After your first run, restart the computer

On the second run enter details.


Note: ReyonMouseFix needs to be in a writeable folder like Documents 



# How To Use


- MouseDPI is DPI of the mouse

- Polling rate: Does nothing for now

- Resolution X is autofilled ( change this with the games resolution if you play full screen e.g 1280x1024)

- Resolution Y is autofilled ( change this with the games resolution if you play full screen e.g 1280x1024)

- Physical Screen X is the width of your monitor SCREEN in millimeter (use manual to find dimensions of your screen)

- Physical Screen Y is the height of your monitor SCREEN in millimeter (use manual to find dimensions of your screen)

- Extra Scale X is Sensitivity, Recommended to try it out but keep it in integer ratios like 12,3 or 0.5, 0.333 etc

- Extra Scale Y is Sensitivity, Recommended to try it out but keep it in integer ratios like 12,3 or 0.5, 0.333 etc

# Contact
**Twitter: https://twitter.com/reyon2g**


**Join us on Discord: https://discord.gg/fUDXq9h***
