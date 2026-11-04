cask "www-posim" do
  version "0.6.9"
  sha256 "5751d3f5aae4d977eb1a105c899042f0ea6d06c4bdbd9f141aaed06562384585"

  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.6.9/WWW-POSIM-0.6.9-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com/"

  depends_on arch: :arm64
  depends_on macos: :golden_gate

  app "WWW-POSIM.app"
end
