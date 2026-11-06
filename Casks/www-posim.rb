cask "www-posim" do
  version "0.6.11"
  sha256 "c32e9db0843f2825076f3f345751633fe380345fadcb69d5b689e03913b0abd0"

  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.6.11/WWW-POSIM-0.6.11-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com/"

  depends_on arch: :arm64
  depends_on macos: :golden_gate

  app "WWW-POSIM.app"
end
