Name:		xkbcomp
Version:	1.2.4
Release:	6
Summary:	Compile XKB keyboard description
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xkbfile) >= 1.0.1
BuildRequires:	x11-util-macros >= 1.0.1

%description
The xkbcomp keymap compiler converts a description of an XKB keymap into one of
several output formats. The most common use for xkbcomp is to create a compiled
keymap file (.xkm extension) which can be read directly by XKB-capable X
servers or utilities.

%package	devel
Summary:	Devel file for xkbcomp
Requires:	%{name} = %{EVRD}

%description	devel
This packages contains the devel file for xkbcomp

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

%files devel
%{_libdir}/pkgconfig/xkbcomp.pc
