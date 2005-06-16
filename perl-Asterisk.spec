#
%include	/usr/lib/rpm/macros.perl
Summary:	Perl modules for interfacing with the Asterisk open source pbx system
Name:		perl-Asterisk
Version:	0.08
Release:	0.1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://asterisk.gnuinter.net/files/asterisk-perl-%{version}.tar.gz
URL:		http://asterisk.gnuinter.net
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(anything_fake_or_conditional)'

%description
These are all modules for interfacing with the Asterisk open source pbx system.

%prep
%setup -q -n asterisk-perl-%{version}

%build
# Don't use pipes here: they generally don't work. Apply a patch.
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/*.agi $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorlib}/Asterisk*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.agi
%{_mandir}/man3/*