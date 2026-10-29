cask "www-posim" do
  version "0.6.1"
  sha256 "685e1e08e600e7545b623fc04c0c8ef50fa48707b9d5abb846fcd5b6092cbab7"

  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.6.1/WWW-POSIM-0.6.1-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com/"

  depends_on arch: :arm64
  depends_on macos: :golden_gate

  app "WWW-POSIM.app"
end
