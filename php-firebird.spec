%define modname firebird
%define dirname interbase
%define soname interbase.so
%define inifile 42_%{modname}.ini

Summary:	Firebird database module for PHP
Name:		php-%{modname}
Epoch:		3
Version:	5.2.7
Release:	%mkrel 1
Group:		Development/PHP
URL:		http://www.php.net
License:	PHP License
Source0:	%{modname}.ini
BuildRequires:	php-devel >= 3:5.2.0
BuildRequires:	firebird-devel
Provides:	php-interbase = %{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is a dynamic shared object (DSO) for PHP that will add Firebird
database support.

%prep

%setup -c -T
cp -dpR %{_usrsrc}/php-devel/extensions/%{dirname}/* .

%build
%serverbuild

phpize
%configure2_5x \
	--with-libdir=%{_lib} \
	--with-interbase=%{_libdir}/firebird

%make
mv modules/*.so .

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot} 

install -D -m0755 %{soname} %{buildroot}%{_libdir}/php/extensions/%{soname}
install -D -m0644 %{SOURCE0} %{buildroot}%{_sysconfdir}/php.d/%{inifile}

%post
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
	%{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc CREDITS
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/php.d/%{inifile}
%attr(0755,root,root) %{_libdir}/php/extensions/%{soname}
