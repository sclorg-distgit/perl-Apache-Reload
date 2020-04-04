%{?scl:%scl_package perl-Apache-Reload}

Name:           %{?scl_prefix}perl-Apache-Reload
Version:        0.13
Release:        13%{?dist}
Summary:        Reload changed Perl modules
License:        ASL 2.0
URL:            https://metacpan.org/release/Apache-Reload
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHAY/Apache-Reload-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl-interpreter
BuildRequires:  %{?scl_prefix}perl-generators
# Apache::Reload from ./lib is loaded
BuildRequires:  %{?scl_prefix}perl(Config)
# ExtUtils::MakeMaker not used because we build for mod_perl-2 only
# File::Spec not used because we build for mod_perl-2 only
BuildRequires:  %{?scl_prefix}perl(lib)
# mod_perl not used
BuildRequires:  %{?scl_prefix}perl(mod_perl2) >= 1.99022
BuildRequires:  %{?scl_prefix}perl(ModPerl::MM)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(vars)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Apache2::Connection)
BuildRequires:  %{?scl_prefix}perl(Apache2::Const)
BuildRequires:  %{?scl_prefix}perl(Apache2::RequestUtil)
BuildRequires:  %{?scl_prefix}perl(Apache2::ServerUtil)
BuildRequires:  %{?scl_prefix}perl(ModPerl::Util)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Tests:
# All tests will be skipped if Apache::Test 1.34, etc. or Test::More is not
# availabe.
# Apache::Constants not used
BuildRequires:  %{?scl_prefix}perl(Apache::Test) >= 1.34
BuildRequires:  %{?scl_prefix}perl(Apache::TestMM)
BuildRequires:  %{?scl_prefix}perl(Apache::TestRunPerl)
BuildRequires:  %{?scl_prefix}perl(Apache::TestRequest)
BuildRequires:  %{?scl_prefix}perl(Apache::TestUtil)
BuildRequires:  %{?scl_prefix}perl(Apache2::RequestIO)
BuildRequires:  %{?scl_prefix}perl(Apache2::RequestRec)
BuildRequires:  %{?scl_prefix}perl(File::Spec::Functions)
BuildRequires:  %{?scl_prefix}perl(Test::More)
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
# The mod_perl2 1.99022 is not used, pick for example ModPerl::Util to
# constrain the version.
Requires:       %{?scl_prefix}perl(ModPerl::Util) >= 1.99022
Conflicts:      mod_perl < 2.0.10-4

# Fiter-underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\(ModPerl::Util\\)$

%description
This mod_perl extension allows to reload Perl modules that changed on the disk.

%prep
%setup -q -n Apache-Reload-%{version}

%build
# MOD_PERL_2_BUILD=1 requires MP_APXS variable set to the apxs executable.
# Use MOD_PERL=2 argument instead.
unset MOD_PERL_2_BUILD
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 MOD_PERL=2 && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc LICENSE
# RELEASE is not for users
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jan 03 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-13
- SCL

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-11
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-8
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 24 2017 Petr Pisar <ppisar@redhat.com> 0.13-5
- This package replaces code bundled to mod_perl
