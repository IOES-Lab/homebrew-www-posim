# IOES-Lab WWW-POSIM distribution

Homebrew tap `ioes-lab/www-posim`, installer releases and Cask metadata for WWW-POSIM, the World Wide Web Platform for Ocean Simulation.

The Apple Silicon application includes ROS 2, Gazebo, Metal rendering, Autopilot and the browser workbench. Version 0.4.2 requires macOS 27 or later. Ubuntu and Windows releases contain compiled desktop clients that run the matching simulator Docker images. Release archives include upstream source and license notices.

```sh
brew tap ioes-lab/www-posim
brew trust --cask ioes-lab/www-posim/www-posim
brew install --cask ioes-lab/www-posim/www-posim
```

For an existing installation from the previous tap:

```sh
brew tap ioes-lab/www-posim
brew trust --cask ioes-lab/www-posim/www-posim
brew reinstall --cask ioes-lab/www-posim/www-posim
brew untap woensug-choi/www-posim
```

User models, cached terrain and projects are stored outside the app and retained during reinstallation.

If Homebrew requests `packages.arm64_dunno.jws.json` and returns HTTP 404 on macOS 27, update Homebrew's OS version support without its package API:

```sh
HOMEBREW_NO_INSTALL_FROM_API=1 brew update
HOMEBREW_NO_AUTO_UPDATE=1 brew tap ioes-lab/www-posim
HOMEBREW_NO_AUTO_UPDATE=1 brew trust --cask ioes-lab/www-posim/www-posim
HOMEBREW_NO_AUTO_UPDATE=1 brew install --cask ioes-lab/www-posim/www-posim
```

These options apply only to the command they precede; see [Homebrew's environment options](https://docs.brew.sh/Manpage#environment). You can also download the [macOS DMG](https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.4.2/WWW-POSIM-0.4.2-macos-arm64.dmg) and drag the app to Applications.

On Mac, the first launch unpacks the native engine once. Sign in with your email account; the platform account address is supplied automatically. User projects and terrain are stored outside the application. The development Mac distribution uses ad-hoc signatures rather than Apple notarization.

The release workflow verifies exact byte counts and SHA-256 checksums against the tested packages before publishing. Each release includes `SHA256SUMS` and `simulator-packages.json`. The ROS command connector is independently versioned.

Classroom templates and the Evaluation client are separate applications.

[IOES-Lab, KMOU](https://lab.wschoi.com)
