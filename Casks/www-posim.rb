cask "www-posim" do
  version "0.5.4"
  sha256 "a76895907825a14d311d9dc0afd0f5f6878cd1de13c9850fa330f469e7f13237"

  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.5.4/WWW-POSIM-0.5.4-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com/"

  depends_on arch: :arm64
  depends_on macos: :golden_gate

  app "WWW-POSIM.app"
end
