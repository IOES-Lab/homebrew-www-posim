cask "www-posim" do
  version "0.5.12"
  sha256 "d8e4224e00225a8dd6343470426d345b23d5f1f18abd6a0f11794a6d1f5f963e"

  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.5.12/WWW-POSIM-0.5.12-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com/"

  depends_on arch: :arm64
  depends_on macos: :golden_gate

  app "WWW-POSIM.app"
end
