WWW-POSIM 0.5.1 includes an Apple Silicon Mac DMG and application-only update, Ubuntu AMD64 DEB and Windows x64 EXE installers.

- POSIM uses upstream revision `487c922`, with subsecond pressure timestamps, bounded DVL layers, safe sensor shutdown, manual-control cleanup and world paths containing spaces.
- The desktop voyage preview fills the available window height. Mobile layouts keep the scene and sensor panels readable.
- The voyage visits 92 stops and uses the current coastal routing and rough-water thresholds.
- Local ROS controllers have an acquisition grace window before their first command.

The Mac app includes ROS 2 Lyrical, Gazebo Jetty 10, Metal rendering, surface and underwater Autopilot, and the web workspace. Application-only updates reuse a matching installed engine. Projects and terrain remain outside the app bundle.

Mac requirements: Apple Silicon, macOS 27 or later. The app is ad-hoc signed and has no Apple notarization. Verify downloads with SHA256SUMS.

Ubuntu and Windows packages use Docker; Windows requires its WSL2 engine. Their matching simulator images require registry read access while the organization keeps those images private. The native Mac app includes its engine.

[Installation](https://www-posim.vercel.app/guide/downloads.html) · [Server status](https://www-posim.vercel.app/status) · [LIVE voyage guide](https://www-posim.vercel.app/guide/voyage.html) · [Feature films](https://www-posim.vercel.app/guide/features.html)
