cask "www-posim" do
  version "0.5.17"
  sha256 "950f7d9662e5dad031261f3a0e764735331d2a0cab559eeb38bc772b929e3aea"

  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.5.17/WWW-POSIM-0.5.17-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com/"

  depends_on arch: :arm64
  depends_on macos: :golden_gate

  app "WWW-POSIM.app"
end
