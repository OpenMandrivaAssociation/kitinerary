%define major 5
%define libname %mklibname KPimItinerary %{major}
%define devname %mklibname KPimItinerary -d

Name: 		kitinerary
Version:	18.08.3
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	1
Source0: http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
Summary:	Library for handling Itinerary data
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Mime)
BuildRequires: cmake(KF5CalendarCore)
BuildRequires: cmake(KF5Contacts)
BuildRequires: cmake(KPimPkPass)
BuildRequires: pkgconfig(zlib)

%description
Library for handling Itinerary data

%package -n %{libname}
Summary: Library for handling Itinerary data
Group: System/Libraries
Requires: %{name} >= %{EVRD}

%description -n %{libname}
Library for handling Itinerary data

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%{_sysconfdir}/xdg/org_kde_kitinerary.categories

%files -n %{libname}
%{_libdir}/libKPimItinerary.so.%{major}*

%files -n %{devname}
%{_includedir}/KPim/KItinerary
%{_includedir}/KPim/kitinerary
%{_libdir}/*.so
%{_libdir}/cmake/*
