# YaPB Graph Database

This repository contains the graph files (waypoints) that [YaPB](https://github.com/yapb/yapb) can download whenever an Internet connection is available.

If you need a waypoint for your map, please open an Issue Request so someone can make it for you. Even better, try making it yourself.

Note to waypoint creators: if you start working on a waypoint request, leave a comment saying so. This avoids duplicated work by another waypoint creator.

## Tutorial on how to make the waypoints
* English: https://yapb.github.io/docs/en/waypointing/
* Russian: https://yapb.github.io/docs/ru/waypointing/

## Uploading graph files
You can upload your work by issuing `yb graph upload`. The bot uploads your graph files to the database. Note that a graph file must pass internal sanity checks and look correct, otherwise it will not be uploaded.

You cannot overwrite existing graph files. If you believe you have created a better one, please open an Issue Request.

By uploading a graph file you agree to release it under the [CC BY-SA 4.0](LICENSE-GRAPH) license that covers this database.

## [Credits](CREDITS.md)
Since YaPB v4.2.698, when a graph file is modified, the original author's name is preserved. The modifier's nickname is also shown with the addition "Modified by: (nickname)".

Note that the modifier's nickname is not shown on previous versions of the bot.

## Licensing

* Everything except the graph files (this README, scripts, workflows, etc.) is released into the public domain under the [Unlicense](LICENSE).
* The graph files (all files under `graph/`) are licensed under [CC BY-SA 4.0](LICENSE-GRAPH).

The credits file is generated from the graph files, so authorship information for individual waypoints is preserved in [CREDITS.md](CREDITS.md). The license on the graph files as a whole does not override the rights of the individual waypoint authors listed there.

