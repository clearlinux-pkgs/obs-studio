#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v2
# autospec commit: f032afc
#
Name     : obs-studio
Version  : 27.2.4
Release  : 53
URL      : https://github.com/obsproject/obs-studio/archive/27.2.4/obs-studio-27.2.4.tar.gz
Source0  : https://github.com/obsproject/obs-studio/archive/27.2.4/obs-studio-27.2.4.tar.gz
Summary  : OBS Studio Library
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause GPL-2.0 LGPL-2.1 MIT
BuildRequires : Vulkan-Headers-dev Vulkan-Loader-dev Vulkan-Tools
BuildRequires : alsa-lib-dev
BuildRequires : buildreq-cmake
BuildRequires : curl-dev
BuildRequires : extra-cmake-modules pkgconfig(egl)
BuildRequires : extra-cmake-modules pkgconfig(libpulse)
BuildRequires : extra-cmake-modules pkgconfig(wayland-client)
BuildRequires : extra-cmake-modules pkgconfig(x11-xcb)
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : freetype-dev
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : mesa-dev
BuildRequires : not-ffmpeg-dev
BuildRequires : pipewire-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(jansson)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libpci)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(libvlc)
BuildRequires : pkgconfig(luajit)
BuildRequires : pkgconfig(speexdsp)
BuildRequires : pkgconfig(vulkan)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-cursor)
BuildRequires : pkgconfig(wayland-egl)
BuildRequires : pkgconfig(wayland-server)
BuildRequires : pkgconfig(x11-xcb)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : pkgconfig(zlib)
BuildRequires : python3-dev
BuildRequires : qtbase-dev
BuildRequires : qtsvg-dev
BuildRequires : qtx11extras-dev
BuildRequires : speex-dev
BuildRequires : speexdsp-dev
BuildRequires : swig
BuildRequires : texlive
BuildRequires : v4l-utils-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: build-without-libx264.patch
Patch2: obs-studio-change-default-config-to-ffmpeg.patch

%description
RNNoise is a noise suppression library based on a recurrent neural network.
To compile, just type:
% ./autogen.sh
% ./configure
% make

%prep
%setup -q -n obs-studio-27.2.4
cd %{_builddir}/obs-studio-27.2.4
%patch -P 1 -p1
%patch -P 2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1697758068
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake .. -DOBS_MULTIARCH_SUFFIX=64 -DBUILD_VST=OFF -DBUILD_BROWSER=OFF
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake .. -DOBS_MULTIARCH_SUFFIX=64 -DBUILD_VST=OFF -DBUILD_BROWSER=OFF
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1697758068
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/obs-studio
cp %{_builddir}/obs-studio-%{version}/COPYING %{buildroot}/usr/share/package-licenses/obs-studio/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/obs-studio-%{version}/UI/data/license/gplv2.txt %{buildroot}/usr/share/package-licenses/obs-studio/53ae571e8630014de689edff14f755f16e5db8ed || :
cp %{_builddir}/obs-studio-%{version}/UI/data/license/gplv2.txt %{buildroot}/usr/share/package-licenses/obs-studio/53ae571e8630014de689edff14f755f16e5db8ed || :
cp %{_builddir}/obs-studio-%{version}/deps/jansson/LICENSE %{buildroot}/usr/share/package-licenses/obs-studio/26a708b97cbb50e3fce8078dd21d65c8fdd5a605 || :
cp %{_builddir}/obs-studio-%{version}/deps/json11/LICENSE.txt %{buildroot}/usr/share/package-licenses/obs-studio/d40d61b8fa8ecae46da12bd1fce4162af02cff8c || :
cp %{_builddir}/obs-studio-%{version}/deps/libcaption/LICENSE.txt %{buildroot}/usr/share/package-licenses/obs-studio/ac86b1d99268507a73261982375a5f47541247b1 || :
cp %{_builddir}/obs-studio-%{version}/deps/w32-pthreads/COPYING %{buildroot}/usr/share/package-licenses/obs-studio/0aeece1a03fbe9860ded71b2e17445209ad33c77 || :
cp %{_builddir}/obs-studio-%{version}/deps/w32-pthreads/COPYING.LIB %{buildroot}/usr/share/package-licenses/obs-studio/f6c7aa5a4f602a093c50a1d3328d1cb873ffdfc0 || :
cp %{_builddir}/obs-studio-%{version}/plugins/mac-syphon/data/syphon_license.txt %{buildroot}/usr/share/package-licenses/obs-studio/6f68b53b3b12e5b75f296c54be785bc63e553d53 || :
cp %{_builddir}/obs-studio-%{version}/plugins/obs-filters/rnnoise/COPYING %{buildroot}/usr/share/package-licenses/obs-studio/5f8e73e1f293d0f127c2bcad2ab6fc5fa2a58139 || :
cp %{_builddir}/obs-studio-%{version}/plugins/obs-outputs/librtmp/COPYING %{buildroot}/usr/share/package-licenses/obs-studio/6138ce06f16aef800693fb256090749acbabd038 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
