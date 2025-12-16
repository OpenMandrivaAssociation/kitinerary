#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define major 6
%define libname %mklibname KPim6Itinerary
%define devname %mklibname KPim6Itinerary -d

# Optional requirements misdetected as mandatory by
# cmake dependency generator
%define __requires_exclude ^cmake\\(\(ZX|zx\)ing\\)$

Name: 		kitinerary
Version:	25.12.0
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	%{?git:0.%{git}.}2
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/kitinerary/-/archive/%{gitbranch}/kitinerary-%{gitbranchd}.tar.bz2#/kitinerary-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/kitinerary-%{version}.tar.xz
%endif
Summary:	Library for handling Itinerary data
URL: https://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6CalendarCore)
BuildRequires: cmake(KF6Contacts)
BuildRequires: cmake(KPim6Mime)
BuildRequires: cmake(KPim6PkPass)
BuildRequires: cmake(ZXing)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(poppler)
BuildRequires: pkgconfig(poppler-qt6)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(shared-mime-info)
BuildRequires: pkgconfig(openssl)
BuildRequires: phonenumber-devel
BuildRequires: pkgconfig(absl_container_common)
BuildRequires: boost-devel
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt6-qttools-assistant

%rename plasma6-kitinerary

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Library for handling Itinerary data.

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

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/org_kde_kitinerary.categories
%{_libdir}/libexec/kf6/kitinerary-extractor
%{_datadir}/mime/packages/application-vnd-kde-itinerary.xml

%files -n %{libname}
%{_libdir}/libKPim6Itinerary.so*

%files -n %{devname}
%{_includedir}/KPim6/KItinerary
%{_includedir}/KPim6/kitinerary
%{_includedir}/KPim6/*.h
%{_libdir}/cmake/*
