%define		snap 20040629
Summary:	3D data exchange library
Summary(pl.UTF-8):   Biblioteka do wymiany danych 3D
Name:		exg
Version:	0.3.0
Release:	0.%{snap}.1
License:	GPL
Group:		Libraries
# From cvs.gna.org/cvs/underware
Source0:	%{name}-%{snap}.tar.gz
# Source0-md5:	8a6fd472e017f3d21ec04c118199031d
Patch0:		%{name}-ac.patch
URL:		https://gna.org/projects/underware/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-utils
BuildRequires:	doxygen
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
3D data exchange library.

%description -l pl.UTF-8
Biblioteka do wymiany danych 3D.

%package devel
Summary:	Header files for exg library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki exg
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for exg library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki exg.

%package static
Summary:	Static files for exg library
Summary(pl.UTF-8):   Pliki statyczne biblioteki exg
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static files for exg library.

%description static -l pl.UTF-8
Pliki statyczne biblioteki exg.

%prep
%setup -q -n %{name}
#%patch0 -p0

%build
rm -f acinclude.m4
%{__aclocal} -I config
%{__libtoolize}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post 	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{py_sitedir}/%{name}
%attr(755,root,root) %{py_sitedir}/%{name}/*.so*
%{py_sitedir}/%{name}/*.py[co]

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/%{name}.pc
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
