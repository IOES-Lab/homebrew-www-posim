cask "www-posim" do
  version "0.5.26"
  sha256 "24c5431eb6875d660a087e4b4f915ad8e933928fb215d5103229a31043bdad25"

  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.5.26/WWW-POSIM-0.5.26-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com/"

  depends_on arch: :arm64
  depends_on macos: :golden_gate

  app "WWW-POSIM.app"
end
