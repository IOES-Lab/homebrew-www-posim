cask "www-posim" do
  version "0.6.8"
  sha256 "0de92e2c68dd37030a4ad8bb0d09f241d9f80e09a45b9278067cc87c263a1012"

  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.6.8/WWW-POSIM-0.6.8-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com/"

  depends_on arch: :arm64
  depends_on macos: :golden_gate

  app "WWW-POSIM.app"
end
