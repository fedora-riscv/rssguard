Name:           rssguard
Version:        3.6.3
Release:        2%{?dist}
Summary:        Simple yet powerful feed reader

# GPLv3+: main program
# BSD: src/dynamic-shortcuts, src/miscellaneous/simplecrypt,
#      src/network-web/googlesuggest
# AGPLv3: src/network-web/oauth2service
License:        GPLv3+ and BSD and AGPLv3
URL:            https://github.com/martinrotter/rssguard
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

Patch0:         rssguard-3.6.3-fix_install_path.patch
Patch1:         rssguard-3.6.3-unbundle_qtsinglecoreapplication.patch
Patch2:         0001-Fix-238-build.patch

# Qt5WebEngine is only available on those architectures
ExclusiveArch:  %{qt5_qtwebengine_arches}

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5WebEngine)
BuildRequires:  qtsingleapplication-qt5-devel
BuildRequires:  qt5-linguist
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
RSS Guard is simple, light and easy-to-use RSS/ATOM feed aggregator developed
using Qt framework which supports online feed synchronization.

%prep
%autosetup -p1 -n %{name}-%{version}

find src -type f | xargs chmod 0644
chmod 0644 resources/desktop/com.github.rssguard.appdata.xml
sed -i 's/\r$//' README.md
rm -rf src/qtsingleapplication

%build
mkdir build && cd build
lrelease-qt5 ../build.pro
%{qmake_qt5} ../build.pro -r PREFIX=%{_prefix} LIB_INSTALL_DIR=%{_lib}
%make_build

%install
cd build
%make_install INSTALL_ROOT=%{buildroot}
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
* Sat Jun 20 17:07:20 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 3.6.3-2
- Fix library perms

* Fri Jun 19 20:44:52 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 3.6.3-1
- Update to 3.6.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 09 23:44:15 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 3.5.9-1
- Release 3.5.9

* Fri May 31 20:03:55 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 3.5.8-1
- Release 3.5.8

* Thu Apr 04 11:14:04 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 3.5.7-1
- Release 3.5.7

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.5.6-2
- better Qt dep

* Mon Feb 26 2018 Robert-André Mauchin <zebob.m@gmail.com> 3.5.6-1
- Upstream release 3.5.6

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 07 2017 Robert-André Mauchin <zebob.m@gmail.com> 3.5.5-1
- Upstream release 3.5.5

* Wed Nov 01 2017 Robert-André Mauchin <zebob.m@gmail.com> 3.5.4-3
- Unbundle qtsinglecoreapplication
- Correct licensing

* Tue Oct 31 2017 Robert-André Mauchin <zebob.m@gmail.com> 3.5.4-2
- Added ExclusiveArch

* Tue Oct 31 2017 Robert-André Mauchin <zebob.m@gmail.com> 3.5.4-1
- First RPM release
