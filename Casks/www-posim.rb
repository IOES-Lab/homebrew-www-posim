cask "www-posim" do
  version "0.5.3"
  sha256 "c3ed696d954073c2f17be27c9317d15076473bf55a8a14c052613bfb6f5fcbfc"

  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.5.3/WWW-POSIM-0.5.3-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com/"

  depends_on arch: :arm64
  depends_on macos: :golden_gate

  app "WWW-POSIM.app"
end
