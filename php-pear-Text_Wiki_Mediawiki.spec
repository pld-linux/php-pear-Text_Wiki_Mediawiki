%include	/usr/lib/rpm/macros.php
%define		_class		Text
%define		_subclass	Wiki_Mediawiki
%define		_status		alpha
%define		_pearname	Text_Wiki_Mediawiki

Summary:	%{_pearname} - Mediawiki parser for Text_Wiki
Summary(pl):	%{_pearname} - parser Mediawiki dla Text_Wiki
Name:		php-pear-%{_pearname}
Version:	0.0.1
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	83d0fb5d0f777ce378a7240f3d8bc745
URL:		http://pear.php.net/package/Text_Wiki_Mediawiki/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-Text_Wiki >= 1.0.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parses Mediawiki mark-up to tokenize the text for Text_Wiki
renderings. You can see a reference for this syntax here:
http://meta.wikimedia.org/wiki/Help:Editing#The_wiki_markup

In PEAR status of this package is: %{_status}.

%description -l pl
Ta klasa przetwarza oznaczenia Mediawiki w celu podzia³u tekstu z
przeznaczeniem dla Text_Wiki. Opis sk³adni mo¿na znale¼æ pod adresem:
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
