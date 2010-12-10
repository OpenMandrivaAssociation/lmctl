%define rel 8
%define name lmctl
%define version 0.3.2
%define release %mkrel %{rel}

Summary:	Configuration tool for Logitech USB Mice
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Configuration/Hardware
URL:		http://bedroomlan.dyndns.org/~alexios/coding_lmctl.html
BuildRoot:	%_tmppath/%{name}-%{version}-%{release}-buildroot
Source0:	http://www.bedroomlan.org/~alexios/files/SOFTWARE/lmctl/%{name}_%{version}.tar.gz
Source1:	http://www.bedroomlan.org/~alexios/files/SOFTWARE/lmctl/%{name}_%{version}.tar.gz.sig
# (abel) Recognize extra mouse IDs
Patch0:		lmctl-0.3.2-extra-devices.patch.bz2
# (abel) MX518 allows max 1600dpi resolution
Patch1:		lmctl-0.3.2-mx518.patch.bz2
BuildRequires:	libusb-devel
Requires:	logitech-mouse-common

%description
LMCtl can manipulate the special features on recent Logitech USB
mice using Command Line interface. Features that can be controlled
or reported include:

o Wireless status reporting
o Battery charge indication
o Resolution
o SmartScroll.

%prep 
%setup -q -n %{name}-0.3.1
%patch0 -p1 -b .extradevice
%patch1 -p1 -b .mx518

%build
%configure2_5x --bindir=%{_sbindir}
%make

%install
rm -rf  %{buildroot}
%makeinstall_std  
 
%clean
rm -rf %{buildroot}

%files  
%defattr(-,root,root)
%doc AUTHORS COPYING README debian/changelog
%{_sbindir}/*
%{_mandir}/man1/lmctl*
 
 
