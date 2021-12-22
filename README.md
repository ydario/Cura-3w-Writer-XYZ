# XYZWriter
Cura Plugin to save directly to 3w format for XYZ Da Vinc Jr. 1.0 machines.

## Support
Tested on the Da Vinci Jr. with Cura 2.3.1 `by gkotas`

Tested on the Da Vinci Jr. 1.0 Wifi with Cura 4.4.1 `by wolfiem` 

Tested on the Da Vinci Jr. 1.0 3-1 with Cura 4.11 `by ydario` 

Inspired by https://www.thingiverse.com/thing:1915076.

Download files: https://github.com/wolfiems/Cura-3w-Writer-XYZ/releases

## Installation
Follow instructions below to get Cura running with Da Vinci Jr. 

(optional) Install printer definition files (or follow XYXprinting how-to):
1. **move** "davinci_jr_platform.stl" to /Applications/Cura.app/Contents/Resources/resources/meshes/davinci_jr_platform.stl
2. **move** "davinci_jr.def.json" to /Applications/Cura.app/Contents/Resources/resources/definitions/davinci_jr.def.json

Then install this plug-in by following the steps:

1. Download the .zip file from Github: https://github.com/wolfiems/Cura-3w-Writer-XYZ/releases/download/v1.0.0/Cura-3w-Writer-XYZ.zip
2. Extract the contents of the .zip archive (including directory) to Cura's plug-in directory in your installation 
* **Windows** `C:\Program Files\Cura\plugins`
* **Mac OS X** `/Applications/Ultimaker\ Cura.app/Contents/Resources/plugins/plugins`
* **linux** `$home/.local/share/cura/4.11/plugins`
3. (Re)start Cura.

## Requirements
You should download and install **threedub** package to run this plugin.
https://gitlab.com/anthem/py-threedub
Note: threedub requires python2
