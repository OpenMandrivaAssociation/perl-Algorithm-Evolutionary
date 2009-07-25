%define upstream_name    Algorithm-Evolutionary
%define upstream_version 0.69

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    N-point crossover
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Algorithm/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Algorithm::Permute)
BuildRequires: perl(Bit::Vector)
BuildRequires: perl(Clone::Fast)
BuildRequires: perl(Math::Random)
BuildRequires: perl(Object::Array)
BuildRequires: perl(String::Random)
BuildRequires: perl(Test::Output)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Tree::DAG_Node)
BuildRequires: perl(XML::Parser::Style::EasyTree)
BuildRequires: perl(YAML)
BuildRequires: perl(Statistics::Basic)
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*
%{_bindir}/tide_bitstring.pl
%{_bindir}/tide_float.pl
%{_bindir}/canonical-genetic-algorithm.pl
%{_mandir}/man1/tide_bitstring.pl.1*
%{_mandir}/man1/tide_float.pl.1*
%{_mandir}/man1/canonical-genetic-algorithm.pl.1*

