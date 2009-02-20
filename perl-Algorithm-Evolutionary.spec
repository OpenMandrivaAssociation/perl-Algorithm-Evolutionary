
%define realname   Algorithm-Evolutionary
%define version    0.63
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    N-point crossover
Source:     http://www.cpan.org/modules/by-module/Algorithm/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel


BuildArch: noarch

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
%setup -q -n %{realname}-%{version} 

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


