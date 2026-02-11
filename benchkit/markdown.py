"""Markdown report."""
from benchkit.stats import mean, stdev, ci

def format_markdown(results):
    lines = ["## Benchmark Results\n","| Name | Mean | StdDev | CI 95% | Status |","|------|------|--------|--------|--------|"] 
    for r in results:
        m,s = mean(r["times"]), stdev(r["times"])
        lo,hi = ci(r["times"])
        st = "Pass" if r.get("passed",True) else "REGRESSION"
        lines.append(f"| {r['name']} | {m:.3f}s | {s:.3f}s | [{lo:.3f},{hi:.3f}] | {st} |")
    lines.append(f"\n*{len(results)} benchmarks by benchkit*")
    return "\n".join(lines)
