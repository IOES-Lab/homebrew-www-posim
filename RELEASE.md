WWW-POSIM 0.3.3 includes the revised ocean-surface rendering, current feature recordings and updated installation documentation.

The native Apple Silicon application bundles ROS 2, Gazebo, Metal rendering, surface and underwater Autopilot, sensor rendering and local ROS command forwarding. Its exact archived engine passed relocation tests with the original build prefix inaccessible: WAM-V out-and-return, BlueROV2 dive/out-and-return/surface, camera/LiDAR/IMU subscriptions, 157 applied local ROS commands with 9.16 m measured motion, and clean shutdown. The staged and mounted DMG apps passed strict signature verification and native-engine diagnostics.

The compiled Ubuntu DEB has been installed through the signed public APT repository on Ubuntu 24.04 and 26.04. The Windows EXE passed a silent installation and CLI checks in Windows CI. Linux and Windows clients require Docker and access to matching engine/workbench images; native NVIDIA rendering capacity has not been measured.

Requires Apple Silicon and macOS 27 or later for the native Mac package. This development distribution is ad-hoc signed, not Apple-notarized. Verify the download using `SHA256SUMS`. The first launch unpacks the engine into the user's Library; projects and terrain remain outside the app.

```sh
brew tap woensug-choi/www-posim
brew trust --cask woensug-choi/www-posim/www-posim
brew install --cask www-posim
```

Sign in with your WWW-POSIM account and account-server URL. Classroom templates and the Evaluation client are separate applications.

[IOES-Lab, KMOU](https://lab.wschoi.com)
