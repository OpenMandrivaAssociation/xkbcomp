Name:		xkbcomp
Version:	1.4.7
Release:	1
Summary:	Compile XKB keyboard description
Group:		Development/X11
Url:      https://gitlab.freedesktop.org/xorg/app/xkbcomp/
Source0:	https://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
License:	MIT
BuildRequires:	bison
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xkbfile)
BuildRequires:	pkgconfig(xorg-macros)

%description
The xkbcomp keymap compiler converts a description of an XKB keymap into one of
several output formats. The most common use for xkbcomp is to create a compiled
keymap file (.xkm extension) which can be read directly by XKB-capable X
servers or utilities.

%package devel
Summary:	Devel file for xkbcomp
Requires:	%{name} = %{EVRD}

%description devel
This packages contains the devel file for xkbcomp.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/xkbcomp
%doc %{_mandir}/man1/xkbcomp.1*

%files devel
%{_libdir}/pkgconfig/xkbcomp.pc
