cask "www-posim" do
  version "0.6.6"
  sha256 "1185b47f7c3a7e0290b9804e955412b9970f753312172efbfa3d81d8b30aae25"

  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.6.6/WWW-POSIM-0.6.6-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com/"

  depends_on arch: :arm64
  depends_on macos: :golden_gate

  app "WWW-POSIM.app"
end
