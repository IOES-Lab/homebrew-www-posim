cask "www-posim" do
  version "0.5.0"
  sha256 "68708eb2ecd8f8bbbcf7adb795a00eaa92d06c31a96928ec9a7d0be2fa1a9693"
  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.5.0/WWW-POSIM-0.5.0-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com"
  depends_on arch: :arm64
  depends_on macos: :golden_gate
  app "WWW-POSIM.app"
end
