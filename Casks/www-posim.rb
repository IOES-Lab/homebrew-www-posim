cask "www-posim" do
  version "0.5.15"
  sha256 "d98decc6f2c934de178287f9bbf270fdb81ea590f27a4915a35c1204dac2ea85"

  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.5.15/WWW-POSIM-0.5.15-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com/"

  depends_on arch: :arm64
  depends_on macos: :golden_gate

  app "WWW-POSIM.app"
end
