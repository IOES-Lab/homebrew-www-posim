cask "www-posim" do
  version "0.3.8"
  sha256 "926a23f7875b8b19940115496bb4130fb91798b6351202f6c9857af71932d6f2"
  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.3.8/WWW-POSIM-0.3.8-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com"
  depends_on arch: :arm64
  depends_on macos: :golden_gate
  app "WWW-POSIM.app"
end
