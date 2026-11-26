cask "www-posim" do
  version "0.6.19"
  sha256 "3e3bc6195a1735c2b12054aae51517fd81a2bbd00c21f1481f03436db77fe6dc"

  url "https://github.com/IOES-Lab/homebrew-www-posim/releases/download/v0.6.19/WWW-POSIM-0.6.19-macos-arm64.dmg"
  name "WWW-POSIM"
  desc "Ocean robot simulator with native ROS, Gazebo and Metal rendering"
  homepage "https://lab.wschoi.com/"

  depends_on arch: :arm64
  depends_on macos: :golden_gate

  app "WWW-POSIM.app"
end
