# WWW-POSIM distribution

Native Apple Silicon application releases and Homebrew Cask metadata for WWW-POSIM, the World Wide Web Platform for Ocean Simulation.

The Mac application includes ROS 2, Gazebo, Metal rendering, Autopilot and the simulator workbench. Version 0.3.0 targets Apple Silicon with macOS 27 or later. Release archives include upstream source and license notices. Development builds use ad-hoc signatures rather than Apple notarization.

```sh
brew tap woensug-choi/www-posim
brew trust --cask woensug-choi/www-posim/www-posim
brew install --cask www-posim
```

The first launch unpacks the native engine once. Sign in with an account server URL and your email account. User projects and terrain are stored outside the application.

The release workflow checks the exact byte counts and SHA-256 of the acceptance-tested installer before publishing it. An invalid download cannot create a release.

[IOES-Lab, KMOU](https://lab.wschoi.com)
