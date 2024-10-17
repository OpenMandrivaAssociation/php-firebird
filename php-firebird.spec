%define modname firebird
%define soname interbase.so
%define inifile 42_%{modname}.ini

Summary:	Firebird database module for PHP
Name:		php-%{modname}
Epoch:		3
Version:	5.4.4
Release:	2
Group:		Development/PHP
URL:		https://www.php.net
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
cp -dpR %{_usrsrc}/php-devel/extensions/interbase/* .

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


%changelog
* Wed Jun 20 2012 Oden Eriksson <oeriksson@mandriva.com> 3:5.4.4-1mdv2012.0
+ Revision: 806383
- 5.4.4

* Thu May 03 2012 Oden Eriksson <oeriksson@mandriva.com> 3:5.4.1-1
+ Revision: 795390
- 5.4.1

* Sun Jan 15 2012 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.9-1
+ Revision: 761191
- 5.3.9

* Wed Aug 24 2011 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.8-1
+ Revision: 696382
- rebuilt for php-5.3.8

* Fri Aug 19 2011 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.7-1
+ Revision: 695342
- rebuilt for php-5.3.7

* Sun Jun 19 2011 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.7-0.0.RC1.1
+ Revision: 685983
- rebuilt for php-5.3.7RC1

* Thu Apr 28 2011 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.6-1
+ Revision: 659825
- stupid bs / rpm5 or whatever.
- rebuilt for php-5.3.6

* Sat Jan 08 2011 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.5-1mdv2011.0
+ Revision: 629757
- 5.3.5

* Mon Jan 03 2011 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.4-1mdv2011.0
+ Revision: 628062
- 5.3.4

* Thu Nov 25 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.4-0.0.RC1.1mdv2011.0
+ Revision: 600984
- use the correct version

* Wed Nov 24 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.3-2mdv2011.0
+ Revision: 600484
- rebuild

* Sun Oct 24 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.3-1mdv2011.0
+ Revision: 588734
- 5.3.3

* Fri Mar 05 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.2-1mdv2010.1
+ Revision: 514539
- rebuilt for php-5.3.2

* Tue Feb 16 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.2-0.0.RC2.1mdv2010.1
+ Revision: 506497
- rebuilt against php-5.3.2RC2

* Sat Jan 02 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.2-0.0.RC1.1mdv2010.1
+ Revision: 485331
- rebuilt for php-5.3.2RC1

* Sat Nov 21 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.1-1mdv2010.1
+ Revision: 468099
- rebuilt against php-5.3.1

* Sat Oct 03 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.1-0.0.RC1.1mdv2010.0
+ Revision: 452828
- 5.3.1RC1

* Wed Sep 30 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.0-2mdv2010.0
+ Revision: 451269
- rebuild

* Mon Jul 20 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.0-1mdv2010.0
+ Revision: 398147
- 5.3.0

* Sun Jul 19 2009 Raphaël Gertz <rapsys@mandriva.org> 3:5.3.0-0.0.RC2.2mdv2010.0
+ Revision: 397522
- Rebuild

* Mon May 18 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.0-0.0.RC2.1mdv2010.0
+ Revision: 376989
- rebuilt for php-5.3.0RC2

* Sun Mar 01 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.9-1mdv2009.1
+ Revision: 346385
- 5.2.9

* Tue Feb 17 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.9-0.0.RC2.1mdv2009.1
+ Revision: 341473
- 5.2.9RC2

* Mon Feb 02 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.8-1mdv2009.1
+ Revision: 336375
- 5.2.8

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.7-2mdv2009.1
+ Revision: 321727
- rebuild

* Fri Dec 05 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.7-1mdv2009.1
+ Revision: 310266
- rebuilt against php-5.2.7

* Sat Jul 19 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-3mdv2009.0
+ Revision: 238772
- rebuild

* Fri Jul 18 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-2mdv2009.0
+ Revision: 238394
- rebuild

* Fri May 02 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-1mdv2009.0
+ Revision: 200201
- rebuilt for php-5.2.6

* Mon Feb 04 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-2mdv2008.1
+ Revision: 162223
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Nov 11 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-1mdv2008.1
+ Revision: 107588
- 5.2.5
- restart apache if needed

* Sat Sep 01 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.4-1mdv2008.0
+ Revision: 77593
- bump version
- rebuilt against php-5.2.4

* Thu Jun 14 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-2mdv2008.0
+ Revision: 39495
- use distro conditional -fstack-protector

* Fri Jun 01 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-1mdv2008.0
+ Revision: 33790
- rebuilt against new upstream version (5.2.3)

* Thu May 03 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.2-1mdv2008.0
+ Revision: 21311
- rebuilt against new upstream version (5.2.2)


* Thu Feb 08 2007 Oden Eriksson <oeriksson@mandriva.com> 5.2.1-1mdv2007.0
+ Revision: 117456
- rebuilt against new upstream version (5.2.1)

* Thu Nov 16 2006 Marcelo Ricardo Leitner <mrl@mandriva.com> 3:5.2.0-4mdv2007.1
+ Revision: 84900
- Rebuilt against firebird 2.0 final.

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild
    - rebuild
    - rebuilt for php-5.2.0

* Wed Sep 06 2006 Marcelo Ricardo Leitner <mrl@mandriva.com> 3:5.1.6-1mdv2007.0
+ Revision: 60124
- First package, highly based on the spec sent by Philippe Makowski.
- Created package structure for php-firebird.

