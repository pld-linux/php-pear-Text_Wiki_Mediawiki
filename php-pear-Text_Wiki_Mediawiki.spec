%define		_status		alpha
%define		_pearname	Text_Wiki_Mediawiki
Summary:	%{_pearname} - Mediawiki parser for Text_Wiki
Summary(pl.UTF-8):	%{_pearname} - parser Mediawiki dla Text_Wiki
Name:		php-pear-%{_pearname}
Version:	0.2.0
Release:	2
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	07971b99bde81f062054c895404bf9ba
URL:		http://pear.php.net/package/Text_Wiki_Mediawiki/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Text_Wiki >= 1.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parses Mediawiki mark-up to tokenize the text for Text_Wiki
renderings. You can see a reference for this syntax here:
http://meta.wikimedia.org/wiki/Help:Editing#The_wiki_markup

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ta klasa przetwarza oznaczenia Mediawiki w celu podziału tekstu z
przeznaczeniem dla Text_Wiki. Opis składni można znaleźć pod adresem:
http://meta.wikimedia.org/wiki/Help:Editing#The_wiki_markup

Ta klasa ma w PEAR status: %{_status}.

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
%{php_pear_dir}/Text/Wiki/Mediawiki.php
%{php_pear_dir}/Text/Wiki/Parse/Mediawiki
