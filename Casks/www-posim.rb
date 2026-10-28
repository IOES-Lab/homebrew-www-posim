cask "www-posim" do
  version "0.5.27"
  sha256 "aee6fe91b3e5baed9b7c36c03e80cd6d9d7ce556a07ea343ed5a2019a3c180d6"

  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.5.27/WWW-POSIM-0.5.27-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com/"

  depends_on arch: :arm64
  depends_on macos: :golden_gate

  app "WWW-POSIM.app"
end
