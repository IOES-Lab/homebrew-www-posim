cask "www-posim" do
  version "0.3.0"
  sha256 "1fb36d33a8a656ea33cb948f43d0820f57a71fe6cd575e734af231d1ae3f780a"
  url "https://github.com/woensug-choi/homebrew-www-posim/releases/download/v0.3.0/WWW-POSIM-0.3.0-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com"
  disable! date: "2026-10-05", because: "fails the DMG signature check; use the patched release"
  depends_on arch: :arm64
  depends_on macos: :golden_gate
  app "WWW-POSIM.app"
end
