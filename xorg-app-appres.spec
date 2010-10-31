Summary:	appres - list X application resource database
Summary(pl.UTF-8):	appres - wypisywanie bazy danych zasobów aplikacji X
Name:		xorg-app-appres
Version:	1.0.3
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/appres-%{version}.tar.bz2
# Source0-md5:	48d56924f76738872ef6c90f99030e34
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-util-util-macros >= 1.8
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
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/appres
%{_mandir}/man1/appres.1x*
