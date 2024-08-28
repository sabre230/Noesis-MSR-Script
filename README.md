## Disclaimer: 
I did not write this script, nor do I maintain it. 
This repository exists to have another source for the file in case it becomes lost. 
The original file and documentation was sourced from [this link](https://www.vg-resource.com/thread-39767-post-670483.html#pid670483).

Original authors are **ByStander23** (commission), **Joschuka** (Dread plugin), and **M-1** (Dread plugin)

# Noesis-MSR-Script
A Noesis script for viewing Metroid: Samus Returns models

## How to Use
* Put the script inside the Noesis Python folder located inside the plugins folder
* Make sure any PKG files you want to decompress are in the same folder as your plugin, otherwise your file structure will not be correct.
* Decompress the PKG files using MEDS (extract-pkg.py) or QuickBMS (format-msr.py) script
  * MEDS is preferred as it is regularly maintained and platform-agnostic
* Once the files are decompressed, use the BMS script that comes with the Noesis script to rename the textures inside the decompressed PKG of your choice.
* Open Noesis and you should be able to view models and animations correctly

## Notes
* This Noesis script has animation support. You will be prompted to select a folder with the animations you want to load.
  * All the MAN files in it and its subfolders will be loaded.
  * If a model moves strangely, that is because the animation is not meant for it.
  * Use Data Viewer to check individual animations more easily
  * Once everything is loaded, go to: Tools > Data Viewer > Model then under Animations, you'll have all the animation filenames. Simply click on one of them to preview it.
* Samus' animations are broken up into two parts: one set for the legs, and another set for the upper body.
* In the Noesis script, you will see "showHiddenMeshes = False", this setting is for enabling GFX on certain models.
  * Simply flip "False" to "True" in a text editor to enable this setting.
* If a texture is not found, you will find a TXT file under the plugins/python folder named "SR".
  * This will have the missing texture names there so you'll just need to find them and put it next to the model file you're trying to open. (Textures will be in another PKG file)
