cask "www-posim" do
  version "0.5.2"
  sha256 "fbe25bbbe94d40919bc50ec7446a5bdf9427eae43406a7d04f1764008789a372"

  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.5.2/WWW-POSIM-0.5.2-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com/"

  depends_on arch: :arm64
  depends_on macos: :golden_gate

  app "WWW-POSIM.app"
end
