# TODO:
# - runtime Requires if any
%define		kdeframever	5.80
%define		qtver		5.9.0
%define		kfname		kcodecs

Summary:	String encoding
Name:		kf5-%{kfname}
Version:	5.80.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	5548ba60e9ce1fac0528811f28995b48
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gperf
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	ninja
BuildRequires:	qt5-linguist >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kf5-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KCodecs provide a collection of methods to manipulate strings using
various encodings. It supports:

- base64
- uu
- quoted-printable

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core-devel >= %{qtver}
Requires:	cmake >= 2.6.0

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kfname}5_qt --with-qm --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kfname}5_qt.lang
%defattr(644,root,root,755)
%doc README.md
%ghost %{_libdir}/libKF5Codecs.so.5
%attr(755,root,root) %{_libdir}/libKF5Codecs.so.*.*
%{_datadir}/qlogging-categories5/kcodecs.categories
%{_datadir}/qlogging-categories5/kcodecs.renamecategories

%files devel
%defattr(644,root,root,755)
%{_libdir}/libKF5Codecs.so
%{_includedir}/KF5/KCodecs
%{_includedir}/KF5/kcodecs_version.h
%{_libdir}/cmake/KF5Codecs
%{_libdir}/qt5/mkspecs/modules/qt_KCodecs.pri
