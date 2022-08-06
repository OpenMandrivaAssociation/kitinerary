%define major 5
%define libname %mklibname KPimItinerary %{major}
%define devname %mklibname KPimItinerary -d

# Optional requirements misdetected as mandatory by
# cmake dependency generator
%define __requires_exclude ^cmake\\(\(ZX|zx\)ing\\)$

Name: 		kitinerary
Version:	22.07.90
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	1
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Summary:	Library for handling Itinerary data
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Qml)
BuildRequires: qt5-qtqml-private-devel
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Mime)
BuildRequires: cmake(KF5CalendarCore)
BuildRequires: cmake(KF5Contacts)
BuildRequires: cmake(KPimPkPass)
BuildRequires: cmake(ZXing)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(poppler)
BuildRequires: pkgconfig(poppler-qt5)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(shared-mime-info)
BuildRequires: pkgconfig(openssl)
BuildRequires: phonenumber-devel
BuildRequires: pkgconfig(absl_container_common)
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant

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

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories5/org_kde_kitinerary.categories
%{_libdir}/libexec/kf5/kitinerary-extractor
%{_datadir}/mime/packages/application-vnd-kde-itinerary.xml

%files -n %{libname}
%{_libdir}/libKPimItinerary.so.%{major}*

%files -n %{devname}
%{_includedir}/KPim/KItinerary
%{_includedir}/KPim/kitinerary
%{_includedir}/KPim/*.h
%{_libdir}/*.so
%{_libdir}/cmake/*
%doc %{_docdir}/qt5/*.{tags,qch}
