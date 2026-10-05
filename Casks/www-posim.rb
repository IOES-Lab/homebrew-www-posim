cask "www-posim" do
  version "0.3.4"
  sha256 "15de186dbab8f3c1b403ca2d0ccd7a50cfd7f64ff94fdc29ab47296d24458a68"
  url "https://github.com/woensug-choi/homebrew-www-posim/releases/download/v0.3.4/WWW-POSIM-0.3.4-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com"
  depends_on arch: :arm64
  depends_on macos: :golden_gate
  app "WWW-POSIM.app"
end
