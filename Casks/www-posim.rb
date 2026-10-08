cask "www-posim" do
  version "0.4.5"
  sha256 "9ea3b4cc2c11c98f61992235a55701fca06eeed87a63845613d525a9ed941d62"
  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.4.5/WWW-POSIM-0.4.5-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com"
  depends_on arch: :arm64
  depends_on macos: :golden_gate
  app "WWW-POSIM.app"
end
