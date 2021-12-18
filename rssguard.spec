Name:           rssguard
Version:        4.0.4
Release:        %autorelease
Summary:        Simple yet powerful feed reader

# GPLv3+: main program
# BSD: src/dynamic-shortcuts, src/miscellaneous/simplecrypt,
#      src/network-web/googlesuggest
# AGPLv3: src/network-web/oauth2service
License:        GPLv3+ and BSD and AGPLv3
URL:            https://github.com/martinrotter/rssguard
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Fix installation path
Patch0:         rssguard-4.0.4-fix_install_path.patch

# Qt5WebEngine is only available on those architectures
ExclusiveArch:  %{qt5_qtwebengine_arches}

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5WebEngine)
BuildRequires:  qt5-linguist
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
RSS Guard is simple, light and easy-to-use RSS/ATOM feed aggregator developed
using Qt framework which supports online feed synchronization.

%prep
%autosetup -p1 -n %{name}-%{version}

sed -i 's/\r$//' README.md

%build
mkdir build && cd build
lrelease-qt5 ../build.pro
%{qmake_qt5} ../build.pro -r PREFIX=%{_prefix} LIB_INSTALL_DIR=%{_lib}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot} -C build
chmod 0755 %{buildroot}%{_bindir}/%{name}
chmod 0755 %{buildroot}%{_libdir}/lib%{name}.so

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/com.github.rssguard.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/com.github.rssguard.appdata.xml

%files
%doc README.md
%license LICENSE.md
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so
%{_datadir}/applications/com.github.rssguard.desktop
%{_datadir}/icons/hicolor/*/apps/rssguard.png
%{_datadir}/metainfo/com.github.rssguard.appdata.xml

%changelog
%autochangelog
