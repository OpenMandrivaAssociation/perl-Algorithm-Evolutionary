%define upstream_name    Algorithm-Evolutionary
%define upstream_version 0.78_2

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	N-point crossover
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Algorithm/JMERELO/Algorithm-Evolutionary-0.78_2.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version}

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
