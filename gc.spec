Name:    gc
Version: 8.0.4
Release: 1
Summary: A garbage collector for C and C++
License: BSD and GPLv1+
Url:     http://www.hboehm.info/gc/
Source0: http://www.hboehm.info/gc/gc_source/gc-%{version}.tar.gz

BuildRequires: gcc libtool libatomic_ops-devel

%description
The Boehm-Demers-Weiser conservative garbage collector can be
used as a garbage collecting replacement for C malloc or C++ new.

%package devel
Summary: Libraries and header files for %{name} development
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
%autosetup -n %{name}-%{version} -p1


%build
# refresh auto*/libtool to purge rpaths
rm -f libtool libtool.m4
autoreconf -i -f

# See https://bugzilla.redhat.com/show_bug.cgi?id=689877
CPPFLAGS="-DUSE_GET_STACKBASE_FOR_MAIN"; export CPPFLAGS

%configure \
  --disable-static \
  --disable-docs \
  --enable-cplusplus \
  --enable-large-config \
  --enable-threads=posix

%{make_build}


%install
%{make_install}

install -p -D -m644 doc/gc.man  %{buildroot}%{_mandir}/man3/gc.3

## Delete unpackaged files
rm -rfv %{buildroot}%{_datadir}/gc/
rm -fv  %{buildroot}%{_libdir}/lib*.la


%check
make check

%files
%doc AUTHORS ChangeLog README.md
%{_libdir}/libcord.so.1*
%{_libdir}/libgc.so.1*
%{_libdir}/libgccpp.so.1*

%files devel
%doc doc/README.environment doc/README.linux
%{_includedir}/gc.h
%{_includedir}/gc_cpp.h
%{_includedir}/gc/
%{_libdir}/libcord.so
%{_libdir}/libgc.so
%{_libdir}/libgccpp.so
%{_libdir}/pkgconfig/bdw-gc.pc
%{_mandir}/man3/gc.3*


%changelog
* Tue Nov 5 2019 shenyangyang<shenyangyang4@huawei.com> - 8.0.4-1
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:update gc to 8.0.4 to solve build problem of guile

* Wed Sep 25 2019 openEuler Buildteam <buildteam@openeuler.org> - 7.6.12-2
- Modify license

* Thu Aug 29 2019 openEuler Buildteam <buildteam@openeuler.org> - 7.6.12-1
- Package init
