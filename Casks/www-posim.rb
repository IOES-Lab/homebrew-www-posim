cask "www-posim" do
  version "0.6.4"
  sha256 "a9b8f2f3e920af287f9c072d7dac1b493b2aabc9ff17a4194583f8ad8285fd65"

  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.6.4/WWW-POSIM-0.6.4-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com/"

  depends_on arch: :arm64
  depends_on macos: :golden_gate

  app "WWW-POSIM.app"
end
