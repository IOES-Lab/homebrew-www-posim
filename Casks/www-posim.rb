cask "www-posim" do
  version "0.4.1"
  sha256 "00fd6d4a4b50c8c19343536dbbdd1d7f934cae511adaf0d9a7d313966f215c96"
  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.4.1/WWW-POSIM-0.4.1-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com"
  depends_on arch: :arm64
  depends_on macos: :golden_gate
  app "WWW-POSIM.app"
end
