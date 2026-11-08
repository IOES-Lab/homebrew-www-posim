cask "www-posim" do
  version "0.6.13"
  sha256 "8b29022058b53286a4c6a518bb7b6e46af749cd6d3b2b63b1987c5381e0f9a73"

  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.6.13/WWW-POSIM-0.6.13-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com/"

  depends_on arch: :arm64
  depends_on macos: :golden_gate

  app "WWW-POSIM.app"
end
