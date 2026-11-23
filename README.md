# ferronweb

[![PKGBUILD Updater](https://github.com/r1sk01/aur-ferronweb/actions/workflows/pkgbuild.yml/badge.svg)](https://github.com/r1sk01/aur-ferronweb/actions/workflows/pkgbuild.yml)
[![AUR](https://img.shields.io/badge/AUR-ferron-blue?logo=archlinux&logoColor=white)](https://aur.archlinux.org/packages/ferron)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](https://github.com/ferronweb/ferron/blob/develop-3.x/LICENSE)

Arch Linux packages for [Ferron](https://ferron.sh), a fast, modern web server written in Rust.

Four packages, so you can pick the build that suits you: compile from source, take the
prebuilt binary, follow a release candidate, or track the development branch.

## Packages

| Package | Build | Follows | Description |
| --- | --- | --- | --- |
| [`ferron`](/packages/ferron) | source | latest stable | A fast, modern web server written in Rust |
| [`ferronweb`](/packages/ferronweb) | prebuilt | latest stable | A fast, modern web server written in Rust (prebuilt binaries) |
| [`ferron-rc`](/packages/ferron-rc) | source | release candidates | A fast, modern web server written in Rust (release candidate) |
| [`ferron-git`](/packages/ferron-git) | source | `develop-3.x` | A fast, modern web server written in Rust (git) |

All four cover `x86_64`, `i686`, `armv7h`, `aarch64` and `riscv64`, ship a systemd unit,
and set up the `ferron` user. They conflict with each other, and `ferronweb`, `ferron-rc`
and `ferron-git` provide `ferron`, so installing one of them replaces `ferron`.

## Status

<!-- BEGIN GENERATED -->
Last checked: 2026-11-22 00:00 UTC

| Package | Version | AUR |
| --- | --- | --- |
| ferron | 2.8.1-4 | [ferron](https://aur.archlinux.org/packages/ferron) |
| ferronweb | 2.8.1-3 | [ferronweb](https://aur.archlinux.org/packages/ferronweb) |
| ferron-rc | 3.0.0rc.11-4 | [ferron-rc](https://aur.archlinux.org/packages/ferron-rc) |
| ferron-git | 3.0.0rc11.r22.g622271c-4 | [ferron-git](https://aur.archlinux.org/packages/ferron-git) |
<!-- END GENERATED -->

## Choosing a package

**Start with `ferron`.** It builds from source against the latest stable release, which
is what the AUR is for, and it gives you the `ferron` name for `pacman -S ferron` and
`yay ferron`.

Pick something else if you have a reason to:

- **`ferronweb`** installs the same version without waiting for a compile. Useful on a
  slow machine or when you want a working server immediately.
- **`ferron-rc`** tracks the latest release candidate. Expect configuration changes and
  the occasional break, since 3.x is not stable yet.
- **`ferron-git`** follows the `develop-3.x` branch commit by commit. This is the
  unstable option, and it will break.

> [!WARNING]
> `ferron-rc` and `ferron-git` both build Ferron 3.x, which is still a release
candidate series. The configuration format differs from 2.x. Read
[the migration guide](https://ferron.sh) before switching a live server.

## Installing

```bash
yay -S ferron
```

The service is installed but not enabled. To start it:

```bash
sudo systemctl enable --now ferron
```

The default config is written to `/etc/ferron.kdl` and serves `/var/www/ferron` on port
80. It is seeded on first install, and an existing config is never overwritten.

## Upgrading

Upgrades are handled by your AUR helper as usual. The package scripts take care of the
rest:

- **1.x to 2.x**: `ferron.yaml` is converted to `ferron.kdl` with `ferron-yaml2kdl`.
- **2.x to 3.x**: `ferron.kdl` is converted with `ferron-kdl2ferron`.
- **Webroot**: stock files are refreshed so branding stays current. Anything you have
  edited or added is left alone.
- **Service**: restarted automatically when it was running.

Backups are left alongside the originals as `.bak` after each conversion, and nothing is
deleted.

## Updating these packages

A scheduled action checks upstream every day and updates whichever packages have a newer
version. It also republishes when a packaging change does not move the version, so a fix
reaches you without a version bump.

The four packages are built independently and pushed to their own AUR repositories from
one GitHub repository.

<details>

<summary>How it works</summary>

Each morning the workflow resolves the latest versions from `dl.ferron.sh`, then four
parallel jobs do the per-package work: bump `pkgver`, re-checksum the sources, and
regenerate `.SRCINFO`. A final job commits what changed and pushes to GitHub and to each
AUR repository.

Only packages that actually changed are published, so a quiet day produces no commits and
no AUR traffic.

</details>

## License

Ferron is MIT licensed. The packaging in this repository is maintained by
[r1sk01](https://github.com/r1sk01).