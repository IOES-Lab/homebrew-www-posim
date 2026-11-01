cask "www-posim" do
  version "0.6.7"
  sha256 "0606956d7cad433f170e0813650d195c5e7926b46a7f6dd5bfbc85ab76fae776"

  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.6.7/WWW-POSIM-0.6.7-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com/"

  depends_on arch: :arm64
  depends_on macos: :golden_gate

  app "WWW-POSIM.app"
end
