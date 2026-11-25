# ferronweb

[![PKGBUILD Updater](https://github.com/r1sk01/aur-ferronweb/actions/workflows/pkgbuild.yml/badge.svg)](https://github.com/r1sk01/aur-ferronweb/actions/workflows/pkgbuild.yml)
[![AUR](https://img.shields.io/badge/AUR-ferron-blue?logo=archlinux&logoColor=white)](https://aur.archlinux.org/packages/ferron)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](https://github.com/ferronweb/ferron/blob/develop-3.x/LICENSE)

Arch Linux packages for [Ferron](https://ferron.sh), a fast, modern web server written in Rust.

## Packages

| Package | Version | Build | Follows | Description |
| --- | --- | --- | --- | --- |
| [`ferron`](/packages/ferron) | 2.8.1-4 | source | latest stable | A fast, modern web server written in Rust |
| [`ferron-bin`](/packages/ferron-bin) | 2.8.1-1 | prebuilt | latest stable | A fast, modern web server written in Rust (prebuilt binaries) |
| [`ferron-rc`](/packages/ferron-rc) | 3.0.0rc.11-4 | source | release candidates | A fast, modern web server written in Rust (release candidate) |
| [`ferron-git`](/packages/ferron-git) | 3.0.0.rc.11.r22.g622271c-4 | source | `develop-3.x` | A fast, modern web server written in Rust (git) |
| [`ferronweb`](/packages/ferronweb) | 2.8.1-3 | shim | n/a | A fast, modern web server written in Rust (prebuilt binaries) |

<details>

<summary>Last checked 2026-11-25 03:21 UTC</summary>

- Move the prebuilt binary to ferron-bin and make ferronweb a shim

</details>

## License

Ferron is MIT licensed. The packaging in this repository is maintained by
[r1sk01](https://github.com/r1sk01).