cask "www-posim" do
  version "0.6.16"
  sha256 "cd3d4df9eee044e5845dde9946914289f3c089a262fb667b08644bf6b5603ba6"

  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.6.16/WWW-POSIM-0.6.16-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com/"

  depends_on arch: :arm64
  depends_on macos: :golden_gate

  app "WWW-POSIM.app"
end
