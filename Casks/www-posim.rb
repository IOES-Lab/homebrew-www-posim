cask "www-posim" do
  version "0.6.5"
  sha256 "f0156023d8bec7c07c414a7b34d7d867448dd76708c5ca9c4a5ad6e50871925a"

  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.6.5/WWW-POSIM-0.6.5-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com/"

  depends_on arch: :arm64
  depends_on macos: :golden_gate

  app "WWW-POSIM.app"
end
