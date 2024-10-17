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
URL:		https://bedroomlan.dyndns.org/~alexios/coding_lmctl.html
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
 
 


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-8mdv2011.0
+ Revision: 620249
- the mass rebuild of 2010.0 packages

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.3.2-7mdv2010.0
+ Revision: 439562
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.3.2-6mdv2009.1
+ Revision: 350239
- 2009.1 rebuild

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 0.3.2-5mdv2008.1
+ Revision: 140932
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import lmctl


* Tue Jun 06 2006 Charles A Edwards <eslrahc@mandriva.org> 0.3.2-5mdv2007.0
- mkrel
- rebuild

* Wed May 18 2005 Abel Cheung <deaddog@mandriva.org> 0.3.2-4mdk
- Requires logitech-mouse-common, so that mouse can be handled by udev

* Tue May 03 2005 Abel Cheung <deaddog@mandriva.org> 0.3.2-3mdk
- Fix patch1 (MX518 uses hardware button to toggle resolution,
  need not set it via software)

* Tue May 03 2005 Abel Cheung <deaddog@mandriva.org> 0.3.2-2mdk
- Patch0: Recognize more types of mice, taken from logitech_applet
- Patch1: Allows 1200 and 1600dpi resolution (esp. for MX518),
  ported from equivalent patch for logitech_applet
- Move binary to $sbindir
- Use tar.gz with signature instead

* Sat Feb 05 2005 Charles A Edwards <eslrahc@mandrake.org> 0.3.2-1mdk
- 0.3.2 ?

* Sat Jan 24 2004 Charles A Edwards <eslrahc@bellsouth.net> 0.2-1mdk
- first mdk release


