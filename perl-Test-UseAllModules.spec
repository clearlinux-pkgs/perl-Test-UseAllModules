#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-UseAllModules
Version  : 0.17
Release  : 7
URL      : https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/Test-UseAllModules-0.17.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/Test-UseAllModules-0.17.tar.gz
Summary  : 'do use_ok() for all the MANIFESTed modules'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

%description
Test::UseAllModules
=====================
INSTALLATION
To install this module type the following:

%package dev
Summary: dev components for the perl-Test-UseAllModules package.
Group: Development
Provides: perl-Test-UseAllModules-devel = %{version}-%{release}

%description dev
dev components for the perl-Test-UseAllModules package.


%prep
%setup -q -n Test-UseAllModules-0.17

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Test/UseAllModules.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::UseAllModules.3
