WWW-POSIM 0.5.2 includes an Apple Silicon Mac DMG and application-only update, Ubuntu AMD64 DEB and Windows x64 EXE installers.

- The standalone app automatically selects matching public Docker Hub engine and workbench images for its installed version. No image URL entry or registry login is required.
- The installer includes the current English and Korean installation guides.
- The Mac app includes its native ROS 2 Lyrical, Gazebo Jetty, Metal rendering, surface and underwater Autopilot, and web workbench. Application-only updates reuse a matching installed engine.

Mac requirements: Apple Silicon, macOS 27 or later. The app is ad-hoc signed and has no Apple notarization. Verify downloads with SHA256SUMS. Projects and terrain remain outside the app bundle.

Ubuntu and Windows packages use Docker; Windows uses Docker Desktop with WSL2. Matching engine images are public on Docker Hub. The native Mac app includes its engine.

[Installation](https://www-posim.vercel.app/guide/downloads.html) · [Server status](https://www-posim.vercel.app/status) · [LIVE voyage guide](https://www-posim.vercel.app/guide/voyage.html)
