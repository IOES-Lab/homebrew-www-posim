cask "www-posim" do
  version "0.6.3"
  sha256 "842d807c3e3afc89d499ea701d3189dbafe1fa4e4d2762c53c2a50614c333388"

  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.6.3/WWW-POSIM-0.6.3-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com/"

  depends_on arch: :arm64
  depends_on macos: :golden_gate

  app "WWW-POSIM.app"
end
