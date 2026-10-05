WWW-POSIM 0.3.4 adds optional update buttons with the target version, startup progress and a POSIM app icon. Installed simulation engines can run when their version or source fingerprint differs from the account server. Sign-in and usage authorization still apply.

The Apple Silicon DMG includes the previously accepted native Metal engine with WAM-V and BlueROV2 sensors, ROS control and Autopilot validation. This app update reuses that engine. Later matching-engine app updates download a 12.7 MB app overlay instead of the full engine.

Linux and Windows installers were built and checked by GitHub Actions. Mac DMG signatures, mounted executable, real local startup and signed overlay replacement/rollback were verified on Apple Silicon.
