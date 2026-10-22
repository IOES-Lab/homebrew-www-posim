cask "www-posim" do
  version "0.5.19"
  sha256 "f94bbacd4f0037a5762f354fb64d67a46b21a483a289bc62e026eea4d5152c64"

  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.5.19/WWW-POSIM-0.5.19-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com/"

  depends_on arch: :arm64
  depends_on macos: :golden_gate

  app "WWW-POSIM.app"
end
