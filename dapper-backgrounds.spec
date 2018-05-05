%global relnum 28
%global bgname dapperlinux
%global Bg_name DapperLinux

Name:       dapper-backgrounds
Version:    28
Release:    1
Summary:    Dapper Linux Default Desktop Backgrounds

License:    FAL-1.3
URL:        https://github.com/dapperlinux/dapper-backgrounds/
Source0:    %{name}-%{version}.tar.xz

BuildArch:  noarch

Provides:   f%{frelease}-backgrounds
Obsoletes:  f%{frelease}-backgrounds

%description
Dapper-Backgrounds contains the default backgrounds used in Dapper Linux. 
Supports many different desktop environments and screen resolutions.


%package        base
Summary:        Base images for %{Bg_name} %{relnum} default background
License:        CC-BY-SA
Provides:       f%{relnum}-backgrounds-base
Obsoletes:      f%{relnum}-backgrounds-base

%description    base
This package contains base images for %{Bg_name} %{relnum} default background.


%package        kde
Summary:        %{Bg_name} %{relnum} default wallpaper for KDE

Requires:       %{name}-base = %{version}-%{release}
Requires:       kde-filesystem
Provides:       f%{relnum}-backgrounds-kde
Obsoletes:      f%{relnum}-backgrounds-kde

%description    kde
This package contains KDE desktop wallpaper for the %{Bg_name} %{relnum}
default theme.

%package        gnome
Summary:        %{Bg_name} %{relnum} default wallpaper for Gnome and Cinnamon

Requires:       %{name}-base = %{version}-%{release}
Provides:       f%{relnum}-backgrounds-gnome
Obsoletes:      f%{relnum}-backgrounds-gnome

%description    gnome
This package contains GNOME/Cinnamon desktop wallpaper for the
%{Bg_name} %{relnum} default theme.

%package        mate
Summary:        %{Bg_name} %{relnum} default wallpaper for Mate

Requires:       %{name}-base = %{version}-%{release}
Provides:       f%{relnum}-backgrounds-mate
Obsoletes:      f%{relnum}-backgrounds-mate

%description    mate
This package contains MATE desktop wallpaper for the %{Bg_name} %{relnum}
default theme.

%package        xfce
Summary:        %{Bg_name} %{relnum} default background for Xfce4

Requires:       %{name}-base = %{version}-%{release}
Requires:       xfdesktop
Provides:       f%{relnum}-backgrounds-xfce
Obsoletes:      f%{relnum}-backgrounds-xfce

%description    xfce
This package contains Xfce4 desktop background for the %{Bg_name} %{relnum}
default theme.

%prep
%autosetup

%build

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files base
%license FAL-1.3.txt Attribution.txt
%dir %{_datadir}/backgrounds/%{bgname}
%dir %{_datadir}/backgrounds/%{bgname}/default
%{_datadir}/backgrounds/%{bgname}/default/normalish
%{_datadir}/backgrounds/%{bgname}/default/standard
%{_datadir}/backgrounds/%{bgname}/default/ultrahd
%{_datadir}/backgrounds/%{bgname}/default/tv-wide
%{_datadir}/backgrounds/%{bgname}/default/%{bgname}.xml

%files kde
%{_datadir}/wallpapers/%{Bg_name}/

%files gnome
%{_datadir}/gnome-background-properties/%{bgname}.xml

%files mate
%{_datadir}/mate-background-properties/%{bgname}.xml

%files xfce
%{_datadir}/xfce4/backdrops/%{bgname}.png

%changelog
* Sat May  5 2018 Matthew Ruffell <msr50@uclive.ac.nz> - 28
- Updating for DL28

* Fri Nov 17 2017 Matthew Ruffell <msr50@uclive.ac.nz> - 27
- Updating for DL27

* Thu Aug 10 2017 Matthew Ruffell <msr50@uclive.ac.nz> - 26
- Updating for DL26

* Fri Nov  4 2016 Matthew Ruffell <msr50@uclive.ac.nz> - 25.0-1
- Updating for DL25

* Fri Oct 14 2016 Matthew Ruffell <msr50@uclive.ac.nz> - 24.0-1
- Initial Dapper Linux Background Packaging
