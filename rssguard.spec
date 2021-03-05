Name:           rssguard
Version:        3.9.0
Release:        1%{?dist}
Summary:        Simple yet powerful feed reader

# GPLv3+: main program
# BSD: src/dynamic-shortcuts, src/miscellaneous/simplecrypt,
#      src/network-web/googlesuggest
# AGPLv3: src/network-web/oauth2service
License:        GPLv3+ and BSD and AGPLv3
URL:            https://github.com/martinrotter/rssguard
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Fix installation path
Patch0:         rssguard-3.8.0-fix_install_path.patch
# Unbundle qtsinglecoreapplication
Patch1:         rssguard-3.8.4-unbundle_qtsinglecoreapplication.patch

# Qt5WebEngine is only available on those architectures
ExclusiveArch:  %{qt5_qtwebengine_arches}

BuildRequires:  make
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
%{qmake_qt5} ../build.pro -r PREFIX=%{_prefix} LIB_INSTALL_DIR=%{_lib } CONFIG+=ltcg
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
* Fri Mar  5 11:56:40 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 3.9.0-1
- Update to 3.9.0
- Close: rhbz#1932738

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  8 15:13:47 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 3.8.4-1
- Update to 3.8.4
- Close: rhbz#1913107

* Fri Dec 04 23:23:28 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 3.8.3-1
- Update to 3.8.3
- Close rhbz#1899877

* Wed Nov 11 12:21:02 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 3.8.0-1
- Update to 3.8.0
- Close rhbz#1874625

* Sat Aug 29 14:38:25 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 3.7.1-1
- Update to 3.7.1 (#1872522)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 16:57:13 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 3.7.0-1
- Update to 3.7.0 (#1856323)

* Wed Jul 01 2020 Jeff Law <law@redhat.com> - 3.6.3-3
- Disable LTO

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
