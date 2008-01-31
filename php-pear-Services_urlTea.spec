%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	urlTea
%define		_status		alpha
%define		_pearname	Services_urlTea
Summary:	%{_pearname} - PHP interface to urlTea's API
Summary(pl.UTF-8):	%{_pearname} - interfejs PHP do API urlTea
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	2
License:	New BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	95aa6c8252c86a50394b7095bb0e5944
URL:		http://pear.php.net/package/Services_urlTea/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An interface for creating urlTea URL's with their API as well as
looking up destinations of given urlTea URL's.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten udostępnia interfejs do tworzenia adresów URL urlTea
wykorzystując ich API, jak również umożliwia odczytywanie adresu
docelowego podanego adres urlTea.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Services/urlTea
%{php_pear_dir}/Services/urlTea.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Services_urlTea
