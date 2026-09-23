# YaPB Graph Database

This repository contains the graph files (waypoints) that are available to [YaPB](https://github.com/yapb/yapb) for download, when Internet is available.

If you need a waypoint for your map, please fill the Issue Request, so someone could make it for you. Or, even better try to make it yourself.

Note to waypoint creators: if you've started working on a waypoint request, say you're working on it. This will avoid unnecessary work for another waypoint creator.

## Tutorial on how to make the waypoints
* English: https://yapb.github.io/docs/en/waypointing/
* Russian: https://yapb.github.io/docs/ru/waypointing/

## Uploading graph files
You can upload your work with issuing ''yb graph upload''. Bot will upload your graph files to database. Note that graph file should pass internal sanity checks, and should look OK, else it's won't be uploaded.

You cannot overwrite existing graph files, if you believe you created better one, than existing, please fill the Issue Request.

## [Credits](CREDITS.md)
Since YaPB v4.2.698, when modifying a graph file, the name of original author is preserved. The modifier's nickname will also be displayed with the addition "Modified by: (nickname)".

Note that modifier's nickname will not be displayed on previous versions of the bot.

## Licensing

* Everything but the graph files (this README, scripts, workflows, etc.) is released into the public domain under the [Unlicense](LICENSE).
* The graph files (all files under `graph/`) are licensed under [CC BY-SA 4.0](LICENSE-GRAPH).

The credits file is generated from the graph files, so the authorship information for individual waypoints is preserved in [CREDITS.md](CREDITS.md). The license on the graph files as a whole does not override the rights of the individual waypoint authors listed there.

