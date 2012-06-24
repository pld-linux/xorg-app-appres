# $Rev: 3335 $, $Date: 2005-08-27 17:42:47 $
#
Summary:	appres application
Summary(pl):	Aplikacja appres
Name:		xorg-app-appres
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/appres-%{version}.tar.bz2
# Source0-md5:	d08734820d9bff3d9c5d2821ec95c285
Patch0:		appres-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkgconfig >= 0.19
BuildRoot:	%{tmpdir}/appres-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
appres application.

%description -l pl
Aplikacja appres.


%prep
%setup -q -n appres-%{version}
%patch0 -p1


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
%attr(755,root,wheel) %{_bindir}/appres
%{_mandir}/man1/*.1*
