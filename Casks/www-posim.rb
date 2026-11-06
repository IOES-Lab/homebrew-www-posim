cask "www-posim" do
  version "0.6.10"
  sha256 "8f451578195e9eff21fad660dddc083111785c50e4266016485d9743910769b6"

  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.6.10/WWW-POSIM-0.6.10-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com/"

  depends_on arch: :arm64
  depends_on macos: :golden_gate

  app "WWW-POSIM.app"
end
