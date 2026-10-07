WWW-POSIM 0.4.4 includes Apple Silicon Mac DMG and application-only updates, Ubuntu AMD64 DEB and Windows x64 EXE installers. The Mac engine includes ROS 2 Lyrical, Gazebo Jetty 10, Metal rendering and surface/underwater Autopilot.

This release documents configurable mass, inertia and hydrodynamic coefficients: Fossen-based 6-DOF dynamics for underwater vehicles and Wave Sim hull forces for surface craft. It also keeps live camera and map elements running across panel fullscreen changes, prevents panels overlapping voyage statistics, and shows readable session status messages.

The exact relocatable native core passed with its original build prefix hidden: WAM-V and BlueROV2 missions, cameras, LiDAR, IMU, local ROS sensor reception and control, and clean shutdown. The 0.4.4 runtime/workbench overlays were rebuilt and exercised against that core. Python bytecode and Next.js runtime caches are stored outside the signed app resources. The mounted DMG signature, version and engine checksum were checked. Ubuntu and Windows compiled launchers passed installation and diagnostics in platform CI; their local engines use matching Docker images. Registry access is required while those engine packages remain private.

Sign in with your email. The account connection is automatic, with visible startup progress and optional updates. User files and terrain remain outside the application bundle. When the native engine matches, application-only updates reuse it. Public LIVE uses one shared voyage and media downloads directly from the simulation origin. The ten participant feature films retain their verified 0.4.2 captures; public voyage formation media was refreshed on October 7 and playback checked again for 0.4.4.

Mac requirements: Apple Silicon, macOS 27 or later. The development app is ad-hoc signed, not Apple-notarized. Use SHA256SUMS to verify downloaded packages.

[Installation and ROS connection guide](https://www-posim.vercel.app/guide/downloads.html) · [Recorded features](https://www-posim.vercel.app/guide/features.html).
