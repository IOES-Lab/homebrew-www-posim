# Install WWW-POSIM

WWW-POSIM simulates ocean robots with Gazebo, ROS 2 and ArduPilot. Choose your computer below. The download links always select the latest published release.

## Contents

- [Mac](#mac)
- [Windows](#windows)
- [Ubuntu Linux](#ubuntu-linux)
- [Start your first workspace](#start-your-first-workspace)
- [Advanced information](#advanced-information)

## Mac

You need an Apple Silicon Mac with macOS 27 or later.

1. [Download the latest Mac installer](https://www-posim.vercel.app/guide/packages/latest/macos-arm64.dmg).
2. Open the DMG. Drag **WWW-POSIM** into **Applications**.
3. Open WWW-POSIM from Applications.

The Mac app includes the native simulation engine. First launch unpacks it and shows the size, progress and estimated remaining time.

If you already use Homebrew, copy these commands into Terminal:

```sh
brew tap ioes-lab/www-posim
brew trust --cask ioes-lab/www-posim/www-posim
brew install --cask ioes-lab/www-posim/www-posim
```

## Windows

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/). Use its WSL2 setup and restart Windows when requested.
2. Start Docker Desktop and wait until it is ready.
3. [Download the latest Windows installer](https://www-posim.vercel.app/guide/packages/latest/windows-x64.exe), open it and follow the installer steps.
4. Open **WWW-POSIM** from the Start menu.

Keep Docker Desktop running. WWW-POSIM downloads the matching simulation images automatically.

## Ubuntu Linux

Use Ubuntu 26.04 or 24.04 on an x86-64 computer. [Prepare Docker](https://www-posim.vercel.app/guide/downloads.html), then copy these commands into Terminal:

```sh
curl -fL -o www-posim.deb https://www-posim.vercel.app/guide/packages/latest/linux-amd64.deb
sudo apt install ./www-posim.deb
www-posim
```

## Start your first workspace

1. Create an account on [www-posim.vercel.app](https://www-posim.vercel.app).
2. Open your verification email and press **Verify email**.
3. Sign in to the installed app.
4. Create a workspace, choose a vehicle, generate its world and start it.

Use [your first simulation guide](https://www-posim.vercel.app/guide/manual.html) for the next steps. To write code in VS Code, follow [Control with Python](https://www-posim.vercel.app/guide/ros.html). For student submissions, follow [Course & competition](https://www-posim.vercel.app/course/index.html).

## Advanced information

- [Latest SHA-256 checksums](https://www-posim.vercel.app/guide/packages/latest/SHA256SUMS) and [package manifest](https://www-posim.vercel.app/guide/packages/latest/simulator-packages.json) identify the published installer bytes.
- The release workflow verifies installer sizes, hashes and native acceptance before updating the Homebrew cask.
- The Mac distribution uses ad-hoc signing and is not Apple-notarized. Follow [macOS opening instructions](https://www-posim.vercel.app/guide/downloads.html) if macOS blocks the app.
- User projects, models and terrain are stored outside the app and retained during updates.
- Ubuntu and Windows use version-matched public Docker images. The Mac app bundles its native engine.
- The [Python/ROS connector wheel](https://www-posim.vercel.app/guide/packages/latest/ros.whl) has its own version. Full ROS scripts need the prepared app environment.
- On macOS 27, a Homebrew `packages.arm64_dunno.jws.json` 404 may require `HOMEBREW_NO_INSTALL_FROM_API=1 brew update`; then repeat the Homebrew installation commands.

[Full installation guide](https://www-posim.vercel.app/guide/downloads.html) · [Server status](https://www-posim.vercel.app/status) · [IOES-Lab, KMOU](https://lab.wschoi.com)
