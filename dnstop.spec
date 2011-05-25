Summary:	Display various tables of DNS traffic on your network
Summary(pl.UTF-8):	Wyświetlanie różnych zestawień ruchu DNS w sieci
Name:		dnstop
Version:	20110502
Release:	1
License:	BSD-like
Group:		Networking/Utilities
Source0:	http://dns.measurement-factory.com/tools/dnstop/src/%{name}-%{version}.tar.gz
# Source0-md5:	28cb54f3780b27e15df8924235e4e37b
URL:		http://dns.measurement-factory.com/tools/dnstop/
BuildRequires:	libpcap-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dnstop is a libpcap application (ala tcpdump) that displays various
tables of DNS traffic on your network, including tables of source and
destination IP addresses, query types, top level domains and second
level domains.

%description -l pl.UTF-8
dnstop to aplikacja oparta na libpcap (podobnie jak tcpdump)
wyświetlająca zestawienia ruchu DNS w sieci wraz z tabelami źródłowych
i docelowych adresów IP, rodzajów zapytań, domen głównych i drugiego
poziomu.

%prep
%setup -q 

%build
%configure
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcppflags} %{rpmcflags} -I/usr/include/ncurses \
		-DUSE_IPV6=1" \
	LIBS="-lresolv -lnsl -lpcap -lncurses -ltinfo"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install dnstop $RPM_BUILD_ROOT%{_sbindir}
install dnstop.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
