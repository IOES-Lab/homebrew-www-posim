cask "www-posim" do
  version "0.3.1"
  sha256 "2eff9fcec6ade2609d8357ecf1d570ba6b59509f539b06e2cbe8d05376d51f06"
  url "https://github.com/woensug-choi/homebrew-www-posim/releases/download/v0.3.1/WWW-POSIM-0.3.1-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com"
  depends_on arch: :arm64
  depends_on macos: :golden_gate
  app "WWW-POSIM.app"
end
