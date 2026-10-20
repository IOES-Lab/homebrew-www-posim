cask "www-posim" do
  version "0.5.14"
  sha256 "2f1bdeb7f79e9cc5b8472657bdaf3f8b306b498db93a51ea7e386346c383b9fe"

  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.5.14/WWW-POSIM-0.5.14-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com/"

  depends_on arch: :arm64
  depends_on macos: :golden_gate

  app "WWW-POSIM.app"
end
