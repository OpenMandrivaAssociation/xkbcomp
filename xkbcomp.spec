Name:		xkbcomp
Version:	1.0.5
Release:	%mkrel 3
Summary:	Compile XKB keyboard description
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxkbfile-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

%description
The xkbcomp keymap compiler converts a description of an XKB keymap into one of
several output formats. The most common use for xkbcomp is to create a compiled
keymap file (.xkm extension) which can be read directly by XKB-capable X
servers or utilities.

%prep
%setup -q -n %{name}-%{version}

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xkbcomp
%{_mandir}/man1/xkbcomp.1*
