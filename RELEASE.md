Version 0.3.1 fixes preservation of the signed app’s symbolic links when staging the DMG. The staged and mounted DMG apps pass strict code-signature verification, version and native-engine diagnostics.

Native Apple Silicon ocean simulator with bundled ROS 2, Gazebo, Metal rendering, surface and underwater Autopilot, sensors and local ROS command forwarding.

Requires Apple Silicon and macOS 27 or later. This development distribution is ad-hoc signed, not Apple-notarized. Verify the installer against SHA256SUMS. The first launch unpacks the engine into the user's Library; projects and terrain are kept outside the app.

```sh
brew tap woensug-choi/www-posim
brew trust --cask woensug-choi/www-posim/www-posim
brew install --cask www-posim
```

Sign in with your WWW-POSIM account and account-server URL. Classroom templates and the Evaluation client are separate applications.

[IOES-Lab, KMOU](https://lab.wschoi.com)
