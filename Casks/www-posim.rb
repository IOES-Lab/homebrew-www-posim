cask "www-posim" do
  version "0.4.2"
  sha256 "36ea3a987643c7a5436455206b28c425be85e98e5bf62f91b61a08c5578434f7"
  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.4.2/WWW-POSIM-0.4.2-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com"
  depends_on arch: :arm64
  depends_on macos: :golden_gate
  app "WWW-POSIM.app"
end
