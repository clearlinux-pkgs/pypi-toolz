#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : toolz
Version  : 0.11.2
Release  : 30
URL      : https://files.pythonhosted.org/packages/5a/f3/f8c3d075da8d949b12fb12ef934ee12fcce369ff83b60253fc2833f8901c/toolz-0.11.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/5a/f3/f8c3d075da8d949b12fb12ef934ee12fcce369ff83b60253fc2833f8901c/toolz-0.11.2.tar.gz
Summary  : List processing tools and functional utilities
Group    : Development/Tools
License  : BSD-3-Clause
Requires: toolz-license = %{version}-%{release}
Requires: toolz-python = %{version}-%{release}
Requires: toolz-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
Toolz
=====
|Build Status| |Coverage Status| |Version Status|
A set of utility functions for iterators, functions, and dictionaries.

%package license
Summary: license components for the toolz package.
Group: Default

%description license
license components for the toolz package.


%package python
Summary: python components for the toolz package.
Group: Default
Requires: toolz-python3 = %{version}-%{release}

%description python
python components for the toolz package.


%package python3
Summary: python3 components for the toolz package.
Group: Default
Requires: python3-core
Provides: pypi(toolz)

%description python3
python3 components for the toolz package.


%prep
%setup -q -n toolz-0.11.2
cd %{_builddir}/toolz-0.11.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641422977
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/toolz
cp %{_builddir}/toolz-0.11.2/LICENSE.txt %{buildroot}/usr/share/package-licenses/toolz/78653a88ec8550f2d7425fac201e6fa43be4d1dd
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/toolz/78653a88ec8550f2d7425fac201e6fa43be4d1dd

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
