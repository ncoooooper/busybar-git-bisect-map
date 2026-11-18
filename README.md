# Git Bisect Map

See the remaining revision range and good/bad bounds of a local Git bisect without changing it.

Set repo to a local working repository where a default-terms Git bisect is in progress. The companion uses only for-each-ref, rev-list and rev-parse. It counts commits reachable from the bad revision excluding all known good revisions. Unusual merge histories and skipped revisions can increase the actual number of steps.

## Connect the bar

Copy companion/example.json to a private config.json and adjust it for your source. From the project folder run `python3 companion/serve.py --config config.json`. Use Python 3.10+. Set Local companion URL to `http://127.0.0.1:8770/reading` on the emulator and allow local port 8770. On hardware, bind the companion to a trusted LAN interface and set its reachable address. The wheel browses pages. Click refreshes. Start pins or unpins the current page. The last good reading is labeled offline after a source error.

## Run locally

From this folder, run `~/.busy-emulator/bin/busy-emulator dev --once` with BUSY Bar Emulator open. Back exits.

![BUSY Bar front display](screenshots/front-1.png)
