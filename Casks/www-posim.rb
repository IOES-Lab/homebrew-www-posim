cask "www-posim" do
  version "0.6.15"
  sha256 "a08a85f09a545f7b90a2787d7ec288f8cb12970389d8a7aeda7f0cec8696d9ec"

  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.6.15/WWW-POSIM-0.6.15-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com/"

  depends_on arch: :arm64
  depends_on macos: :golden_gate

  app "WWW-POSIM.app"
end
