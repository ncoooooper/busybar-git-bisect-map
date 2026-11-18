"""Read the current local git bisect bounds, candidate count and estimated checks left."""
import math,subprocess
from pathlib import Path
from serve import page
INTERVAL=4
def snapshot(o,m):
    repo=Path(o["repo"]).expanduser()
    def git(*args):return subprocess.check_output(["git","-C",str(repo),*args],text=True,stderr=subprocess.DEVNULL,timeout=5).strip()
    refs=git("for-each-ref","--format=%(refname) %(objectname)","refs/bisect").splitlines()
    labels={r.split()[0].split("/")[-1]:r.split()[1] for r in refs}
    bad=labels.get("bad");good=[sha for k,sha in labels.items() if k.startswith("good-")]
    if not bad or not good:return dict(state="Git bisect",key="no bounds",pages=[page("BISECT","No bounds","Needs good and bad refs","Start bisect in your repo")])
    candidates=int(git("rev-list","--count",bad,"--not",*good));steps=math.ceil(math.log2(max(1,candidates)))
    skipped=sum(k.startswith("skip-") for k in labels)
    return dict(state="Local repository / read only",key=bad+str(candidates),pages=[
       page("CANDIDATES",candidates,f"About {steps} more checks",f"{skipped} skipped refs"),
       page("BAD BOUND",bad[:7],f"{len(good)} good bounds","HEAD "+git("rev-parse","--short","HEAD")),
       page("GOOD BOUND",good[0][:7],"First recorded good bound","Includes merges in range")])
