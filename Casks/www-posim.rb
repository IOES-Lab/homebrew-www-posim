cask "www-posim" do
  version "0.6.12"
  sha256 "72616e86476d49acb2a9620f26e9304d88f4a0fa050f4948bbc2e2c96c7f5b07"

  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.6.12/WWW-POSIM-0.6.12-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com/"

  depends_on arch: :arm64
  depends_on macos: :golden_gate

  app "WWW-POSIM.app"
end
