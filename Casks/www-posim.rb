cask "www-posim" do
  version "0.3.3"
  sha256 "850fa85a7009be90c187051329d2d4d13bfddcb7a2c5ee121dd7444acf2650cc"
  url "https://github.com/woensug-choi/homebrew-www-posim/releases/download/v0.3.3/WWW-POSIM-0.3.3-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com"
  depends_on arch: :arm64
  depends_on macos: :golden_gate
  app "WWW-POSIM.app"
end
