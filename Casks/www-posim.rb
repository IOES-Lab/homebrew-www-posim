cask "www-posim" do
  version "0.4.3"
  sha256 "73cf0e3996b85cbcabb74997877cdbab9603f64fb45728d9d08ba34a82543807"
  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.4.3/WWW-POSIM-0.4.3-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com"
  depends_on arch: :arm64
  depends_on macos: :golden_gate
  app "WWW-POSIM.app"
end
