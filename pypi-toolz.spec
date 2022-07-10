#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-toolz
Version  : 0.12.0
Release  : 34
URL      : https://files.pythonhosted.org/packages/cf/05/2008534bbaa716b46a2d795d7b54b999d0f7638fbb9ed0b6e87bfa934f84/toolz-0.12.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/cf/05/2008534bbaa716b46a2d795d7b54b999d0f7638fbb9ed0b6e87bfa934f84/toolz-0.12.0.tar.gz
Summary  : List processing tools and functional utilities
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-toolz-license = %{version}-%{release}
Requires: pypi-toolz-python = %{version}-%{release}
Requires: pypi-toolz-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
=====
        
        |Build Status| |Coverage Status| |Version Status|
        
        A set of utility functions for iterators, functions, and dictionaries.

%package license
Summary: license components for the pypi-toolz package.
Group: Default

%description license
license components for the pypi-toolz package.


%package python
Summary: python components for the pypi-toolz package.
Group: Default
Requires: pypi-toolz-python3 = %{version}-%{release}

%description python
python components for the pypi-toolz package.


%package python3
Summary: python3 components for the pypi-toolz package.
Group: Default
Requires: python3-core
Provides: pypi(toolz)

%description python3
python3 components for the pypi-toolz package.


%prep
%setup -q -n toolz-0.12.0
cd %{_builddir}/toolz-0.12.0
pushd ..
cp -a toolz-0.12.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657480525
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

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-toolz
cp %{_builddir}/toolz-0.12.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-toolz/78653a88ec8550f2d7425fac201e6fa43be4d1dd
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-toolz/78653a88ec8550f2d7425fac201e6fa43be4d1dd

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
