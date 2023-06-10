# player-converter

Read the Note section before using.

A tool to convert starbound player files across incompatible mods.

Say you created a vanilla character and played it for quite a while. The original limiting inventory size started to bother you so you decided to download an inventory extender. But wait, any inventory extender mod requires a new character, so what do you do?

This is what this script sets out to solve.

Right now it only supports player files going from vanilla to [bk3k's Inventory](https://steamcommunity.com/sharedfiles/filedetails/?id=882900100). Any slot version should work as long as you put in the correct number when it prompts.

# Note
- **IT CLEARS YOUR INVENTORY**<br>In order for this script to work (without me having to do a ton more work), your inventory (and hotbar configuration) will be cleared. Make sure to dump your inventory somewhere before using this script.
- **NOT COMPATABLE WITH HOTBAR EXTENDERS (yet....)**<br>This script as of now is only to change vanilla (and with mods that dont influence inventory or hotbar), to work with bk3k's inventory mod. Anything that messes with the hotbar will cause this script to make your player file crash. Texture mods should be okay, like frackin interface (not tested).
- **NOT REVERSABLE (yet...)**<br>Once you use this script theres no going back to non-bk3k's inventory. I will implement this soon™.
- **BACKUP YOUR STORAGE FOLDER**<br>This is a barely tested script (works in the best conditions) might not work and/or corrupt your stuff for whatever reason on your side. Raise a github issue and I'll look at it, but in the mean time **BACKUP YOUR STORAGE FOLDER!!!!**.

# Usage
First install python.

Then backup your starbound storage directory just in case.

Next install everything from the requirements.txt file. To do this: download and navigate to the project directory in terminal, then enter:

> pip install -r requirements.txt

Now you are set to run it. To do this find the player file in your starbound directory. It will be a bunch of numbers with a '.player' extension. There will be several based on how many players you have. Youll just have to guess for now (ill make a better way soon)

Shift-right click the file and click 'copy as path'.

Then go back to your terminal in the project directory and enter

> python main.py \<path>

where path you can just paste it there. Make sure it is enclosed in quotation marks.

It will prompt you to enter the amount of slots the version of bk3k's inventory you downloaded, make sure this is correct or it will not work.

Then your done!
