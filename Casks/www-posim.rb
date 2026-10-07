cask "www-posim" do
  version "0.4.4"
  sha256 "dc507da6ddfd672cbee9ea7564a6e84d0b323f6968c9679598ddcf2680a9679f"
  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.4.4/WWW-POSIM-0.4.4-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com"
  depends_on arch: :arm64
  depends_on macos: :golden_gate
  app "WWW-POSIM.app"
end
