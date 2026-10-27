cask "www-posim" do
  version "0.5.25"
  sha256 "37ee4f12484d2b47d659cb2257b41a6f664d9e448947d9de2d28a06e14ba62db"

  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.5.25/WWW-POSIM-0.5.25-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com/"

  depends_on arch: :arm64
  depends_on macos: :golden_gate

  app "WWW-POSIM.app"
end
