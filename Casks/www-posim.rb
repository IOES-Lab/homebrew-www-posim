cask "www-posim" do
  version "0.5.18"
  sha256 "4b838f43afb6db61d2c84277f7a615d7161af386921a4862b3f10459177b0243"

  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.5.18/WWW-POSIM-0.5.18-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com/"

  depends_on arch: :arm64
  depends_on macos: :golden_gate

  app "WWW-POSIM.app"
end
