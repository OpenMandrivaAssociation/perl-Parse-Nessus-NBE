%define upstream_name    Parse-Nessus-NBE
%define upstream_version 1.1

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Summary:    Extract information from Nessus NBE files
License:    Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/D/DK/DKYGER/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires: perl(Socket6)
BuildRequires: perl(Net::Frame)
Requires:      perl(Exporter)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module is designed to extract information from Nessus NBE
files. Functions have been designed to return certain sets of data,
such as service banners and OS versions. Other functions have been
provided that will return more specific information, such as all IPs
listening on a given port or all IPs associated with a specified plugin id.

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
%doc Changes README MANIFEST
%{_mandir}/man3/*
%perl_vendorlib/*


