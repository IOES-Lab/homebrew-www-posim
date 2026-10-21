cask "www-posim" do
  version "0.5.16"
  sha256 "1213c56419c01d8fed25f97e19d30276f2f3e06a79d8e795b1ba7226e2761e7d"

  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.5.16/WWW-POSIM-0.5.16-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com/"

  depends_on arch: :arm64
  depends_on macos: :golden_gate

  app "WWW-POSIM.app"
end
