# YaPB Graph Database

This repository contains the graph files (waypoints) that are available to [YaPB](https://github.com/yapb/yapb) for download, when Internet is available.

If you need a waypoint for your map, please fill the Issue Request, so someone could make it for you. Or, even better try to make it yourself.

Note to waypoint creators: if you've started working on a waypoint request, say you're working on it. This will avoid unnecessary work for another waypoint creator.

## Tutorial on how to make the waypoints
* English: https://yapb.readthedocs.io/en/latest/waypointing.html
* Russian: https://yapb.readthedocs.io/ru/latest/waypointing.html

## Uploading graph files
You can upload your work with issuing ''yb graph upload''. Bot will upload your graph files to database. Note that graph file should pass internal sanity checks, and should look OK, else it's won't be uploaded.

You cannot overwrite existing graph files, if you believe you created better one, than existing, please fill the Issue Request.

## Credits
Since YaPB v4.2.698, when modifying a graph file, the name of original author is preserved. The modifier's nickname will also be displayed with the addition "Modified by: (nickname)".

Note that modifier's nickname will not be displayed on previous versions of the bot.
