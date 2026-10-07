# Bouncing Balls Labs

Two Pygame simulations by Eddie Liao, kept as independent programs in one repository.

## Explore

- [Bouncing Ball](bouncing-ball/): gravity, changing colors on impact, and energy loss on vertical bounces.
- [Interacting Circles](interacting-circles/): 100 moving circles with pairwise gravitational attraction, elastic collisions, and wall bounces.

Open the website, choose a simulation, and click its player to start. Both run automatically with no keyboard controls. Refresh a player to restart; use browser Back to return to the menu.

## Preserved originals

Each folder contains an unchanged `original_main.py` and the browser-compatible `main.py`.

- Bouncing Ball: https://onecompiler.com/pygame/453d5vypm
- Interacting Circles: https://onecompiler.com/pygame/4538ubppw

Complete sources retrieved October 7, 2026. The circles assignment title mentions 1000+, but its actual saved source sets `N = 100`; this publication preserves 100. No simulation equations, initial parameters, or collision rules were changed. Both programs are wrapped in an async function and yield instead of using the blocking 60 FPS limiter. The simulation advances one original step per frame, targeting 60 Hz; slower devices may run below that rate.

## Run and rebuild

```sh
python -m pip install -r requirements.txt
python bouncing-ball/main.py
# Or: python interacting-circles/main.py
python build_web.py
python -m http.server 8000
```

Open http://localhost:8000 for the menu. Each player has its own generated index and game archive. First load requires the official pygame-web CDN for the Python/WebAssembly runtime. Vercel uses the Other static preset, no build command, and output directory `.` as specified in `vercel.json`. Rebuild and commit generated files after changing Python code.
