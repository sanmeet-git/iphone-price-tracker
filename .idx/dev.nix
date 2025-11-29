# .idx/dev.nix - Version 4.0 (Final Missing Pieces)
{ pkgs, ... }: {
  channel = "stable-24.05"; 

  packages = [
    # 1. Python Tools
    pkgs.python3
    pkgs.python3Packages.pip
    pkgs.python3Packages.virtualenv
    
    # 2. System Libraries (The "Bones")
    pkgs.glib
    pkgs.nss
    pkgs.nspr
    pkgs.dbus
    pkgs.atk
    pkgs.cups
    pkgs.libdrm
    pkgs.gtk3
    pkgs.pango
    pkgs.cairo
    pkgs.gdk-pixbuf
    pkgs.mesa
    pkgs.alsa-lib
    pkgs.at-spi2-atk
    pkgs.at-spi2-core
    
    # 3. The XORG Libraries
    pkgs.xorg.libX11
    pkgs.xorg.libXcomposite
    pkgs.xorg.libXdamage
    pkgs.xorg.libXext
    pkgs.xorg.libXfixes
    pkgs.xorg.libXrandr
    pkgs.xorg.libxcb
    
    # 4. The Final Missing Pieces (Found in error log)
    pkgs.expat           # libexpat.so.1
    pkgs.libxkbcommon    # libxkbcommon.so.0
    pkgs.systemd         # libudev.so.1 (udev lives inside systemd)
  ];

  env = {
    # This helps Python find the bones we just installed
    LD_LIBRARY_PATH = "${pkgs.stdenv.cc.cc.lib}/lib";
  };

  idx = {
    extensions = [
      "ms-python.python"
    ];
  };
}