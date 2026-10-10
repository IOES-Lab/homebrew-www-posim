cask "www-posim" do
  version "0.5.1"
  sha256 "edfbdaa77e102f8cacba43a88abd46b227946331acfc111e642206d473efbdb7"

  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.5.1/WWW-POSIM-0.5.1-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com/"

  depends_on arch: :arm64
  depends_on macos: :golden_gate

  app "WWW-POSIM.app"
end
