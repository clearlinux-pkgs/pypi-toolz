#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : toolz
Version  : 0.9.0
Release  : 3
URL      : https://files.pythonhosted.org/packages/14/d0/a73c15bbeda3d2e7b381a36afb0d9cd770a9f4adc5d1532691013ba881db/toolz-0.9.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/14/d0/a73c15bbeda3d2e7b381a36afb0d9cd770a9f4adc5d1532691013ba881db/toolz-0.9.0.tar.gz
Summary  : List processing tools and functional utilities
Group    : Development/Tools
License  : BSD-3-Clause
Requires: toolz-license = %{version}-%{release}
Requires: toolz-python = %{version}-%{release}
Requires: toolz-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
=====
        
        |Build Status| |Coverage Status| |Version Status| |Downloads|
        
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

%description python3
python3 components for the toolz package.


%prep
%setup -q -n toolz-0.9.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542925171
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/toolz
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/toolz/LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/toolz/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
