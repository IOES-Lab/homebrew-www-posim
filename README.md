# WWW-POSIM distribution

Installer releases and Homebrew Cask metadata for WWW-POSIM, the World Wide Web Platform for Ocean Simulation.

The Apple Silicon application includes ROS 2, Gazebo, Metal rendering, Autopilot and the browser workbench. Version 0.3.3 requires macOS 27 or later. Ubuntu and Windows releases contain compiled desktop clients that run the matching simulator Docker images. Release archives include upstream source and license notices.

```sh
brew tap woensug-choi/www-posim
brew trust --cask woensug-choi/www-posim/www-posim
brew install --cask www-posim
```

On Mac, the first launch unpacks the native engine once. Sign in with an account server URL and your email account. User projects and terrain are stored outside the application. The development Mac distribution uses ad-hoc signatures rather than Apple notarization.

The release workflow verifies exact byte counts and SHA-256 checksums against the tested packages before publishing. Each release includes `SHA256SUMS` and `simulator-packages.json`. The ROS command connector is independently versioned.

Classroom templates and the Evaluation client are separate applications.

[IOES-Lab, KMOU](https://lab.wschoi.com)
