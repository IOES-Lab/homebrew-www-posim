cask "www-posim" do
  version "0.5.13"
  sha256 "e07d2e95b5b1cd02594780d063d373aee9e9ec498f85a006e32e3c701854e1f9"

  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.5.13/WWW-POSIM-0.5.13-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com/"

  depends_on arch: :arm64
  depends_on macos: :golden_gate

  app "WWW-POSIM.app"
end
