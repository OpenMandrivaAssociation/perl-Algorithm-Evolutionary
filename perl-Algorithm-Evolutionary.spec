%define upstream_name    Algorithm-Evolutionary
%define upstream_version 0.762

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	N-point crossover
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Algorithm/%{upstream_name}-0.76_2.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Algorithm::Permute)
BuildRequires:	perl(B::Deparse)
BuildRequires:	perl(Bit::Vector)
BuildRequires:	perl(Clone)
BuildRequires:	perl(Clone::Fast)
BuildRequires:	perl(GD::Image)
BuildRequires:	perl(Math::Random)
BuildRequires:	perl(Memoize)
BuildRequires:	perl(Object::Array)
BuildRequires:	perl(Pod::Escapes)
BuildRequires:	perl(Statistics::Basic)
BuildRequires:	perl(String::Random)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Output)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Simple)
BuildRequires:	perl(Time::HiRes)
BuildRequires:	perl(Tree::DAG_Node)
BuildRequires:	perl(XML::LibXML)
BuildRequires:	perl(XML::Parser)
BuildRequires:	perl(XML::Parser::Style::EasyTree)
BuildRequires:	perl(YAML)
BuildRequires:	perl(Statistics::Basic)
BuildArch:	noarch

%description
'Algorithm::Evolutionary' is a set of classes for doing object-oriented
evolutionary computation in Perl. Why would anyone want to do that escapes
my knowledge, but, in fact, we have found it quite useful for our own
purposes. Same as Perl itself.

The design principle of Algorithm::Evolutionary is _flexibility_: it should
be very easy to extend using this library, and it should be also quite easy
to program what's already there in the evolutionary computation community.
Besides, the library classes should have persistence provided by XML
modules, and, in some cases, YAML.

The algorithm allows to create simple evolutionary algorithms, as well as
more complex ones, that interface with databases or with the web. 

%prep
%setup -q -n %{upstream_name}-0.76_2

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*
%{_bindir}/rectangle-coverage.pl
%{_bindir}/tide_bitstring.pl
%{_bindir}/tide_float.pl
%{_bindir}/canonical-genetic-algorithm.pl


%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.762.0-1mdv2011.0
+ Revision: 658815
- add br
- new version 0.762
- rebuild for updated spec-helper

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Wed Mar 17 2010 Jérôme Quelin <jquelin@mandriva.org> 0.730.0-1mdv2010.1
+ Revision: 523430
- update to 0.73

* Wed Jan 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.720.0-1mdv2010.1
+ Revision: 496998
- update to 0.72

* Tue Sep 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.710.0-1mdv2010.0
+ Revision: 442631
- update to 0.71

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.700.0-2mdv2010.0
+ Revision: 408705
- adding missing buildrequires:
- force rebuild
- update to 0.70

* Sat Jul 25 2009 Jérôme Quelin <jquelin@mandriva.org> 0.690.0-1mdv2010.0
+ Revision: 399656
- adding missing buildrequires:
- adding missing buildrequires:
- update to 0.69
- using %%perl_convert_version
- fixed license field

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.67-2mdv2010.0
+ Revision: 375968
- rebuild

* Sun May 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.67-1mdv2010.0
+ Revision: 371227
- new version

* Thu Mar 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.64-1mdv2009.1
+ Revision: 357730
- new version

* Sun Mar 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.63-1mdv2009.1
+ Revision: 355238
- adding missing build requires
- import perl-Algorithm-Evolutionary


* Fri Feb 20 2009 cpan2dist 0.63-1mdv
- initial mdv release, generated with cpan2dist

