Summary:	appres - list X application resource database
Summary(pl.UTF-8):	appres - wypisywanie bazy danych zasobów aplikacji X
Name:		xorg-app-appres
Version:	1.0.6
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/appres-%{version}.tar.xz
# Source0-md5:	16d585015ea01f80efd2a3a151152b0c
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.17
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The appres program prints the resources seen by an application (or
subhierarchy of an application) with the specified class and instance
names. It can be used to determine which resources a particular
program will load.

%description -l pl.UTF-8
Program appres wypisuje zasoby widziane przez aplikację (lub
podhierarchię aplikacji) o określonej nazwie klasy i instancji. Może
być używany do określenia, które zasoby wczytuje dany program.

%prep
%setup -q -n appres-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/appres
%{_mandir}/man1/appres.1*
