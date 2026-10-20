WWW-POSIM 0.5.12 includes the Apple Silicon Mac DMG and app-only update, Windows x64 installer, Ubuntu AMD64 DEB, and the independently versioned ROS connector 0.4.0.

- Native Mac rendering includes the WAM-V wave surface and BlueROV cutaway. The native engine uses a 10 ms integration interval.
- ROS control and camera/IMU/LiDAR access are documented with Python examples. Camera frames can be saved from the workspace.
- The workspace includes regional maps, sensor selection, startup progress and the message that startup may take up to five minutes.
- Windows and Linux automatically select the matching public 0.5.12 engine and workbench images. Mac includes its native ROS 2 Lyrical, Gazebo Jetty and Metal engine.

Mac requires Apple Silicon and macOS 27 or later. The app is ad-hoc signed; it is not Apple notarized. Verify downloads with SHA256SUMS. Projects and terrain remain outside the app bundle. The app-only update requires the matching accepted native engine already installed.

Windows uses Docker Desktop with WSL2. Ubuntu uses Docker. Use the same verified account as the website.

[Install and download](https://www-posim.vercel.app/guide/downloads.html) · [ROS setup and examples](https://www-posim.vercel.app/guide/ros.html) · [Server status](https://www-posim.vercel.app/status)
