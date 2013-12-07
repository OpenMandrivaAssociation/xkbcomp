Name:		xkbcomp
Version:	1.2.4
Release:	5
Summary:	Compile XKB keyboard description
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: pkgconfig(xkbfile) >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

%description
The xkbcomp keymap compiler converts a description of an XKB keymap into one of
several output formats. The most common use for xkbcomp is to create a compiled
keymap file (.xkm extension) which can be read directly by XKB-capable X
servers or utilities.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_bindir}/xkbcomp
%{_mandir}/man1/xkbcomp.1*
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Tue Mar 27 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.4-1
+ Revision: 787150
- version update 1.2.4

* Sat Sep 10 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.3-1
+ Revision: 699284
- update to new version 1.2.3

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-2
+ Revision: 671327
- mass rebuild

* Fri Feb 11 2011 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.2.1-1
+ Revision: 637251
- New version: 1.2.1

* Tue Nov 02 2010 Thierry Vignaud <tv@mandriva.org> 1.2.0-1mdv2011.0
+ Revision: 591826
- new release

* Wed Nov 11 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.1.1-1mdv2010.1
+ Revision: 464710
- New version: 1.1.1

* Thu Jul 09 2009 Thierry Vignaud <tv@mandriva.org> 1.1.0-1mdv2010.0
+ Revision: 393772
- new release

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.5-3mdv2009.1
+ Revision: 351043
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.0.5-2mdv2009.0
+ Revision: 266091
- rebuild early 2009.0 package (before pixel changes)

* Wed May 28 2008 Thierry Vignaud <tv@mandriva.org> 1.0.5-1mdv2009.0
+ Revision: 212576
- new release

* Mon Apr 14 2008 Thierry Vignaud <tv@mandriva.org> 1.0.4-1mdv2009.0
+ Revision: 192975
- new release

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-3mdv2008.1
+ Revision: 154693
- Updated BuildRequires and resubmit package.
  This program deserves a mandriva branch in git, but since the only changes
  from tag xkbcomp-1.0.3 are updated COPYING and changes in source to declare
  char * as const char *, will leave possible adition of branch to later, and
  if required.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 15 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.0.3-2mdv2008.1
+ Revision: 98612
- minor spec cleanup
- rebuild with xserver 1.4 and latest x11proto
  (just in case)

* Fri Aug 31 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.3-1mdv2008.0
+ Revision: 76530
- rebuild for 2008
- new release 1.0.3
- slight spec clean

  + Thierry Vignaud <tv@mandriva.org>
    - do not hardcode lzma extension!!!

