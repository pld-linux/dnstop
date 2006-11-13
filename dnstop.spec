Summary:	Display various tables of DNS traffic on your network
Summary(pl):	Wy¶wietlanie ró¿nych zestawieñ ruchu DNS w sieci
Name:		dnstop
Version:	20060517
Release:	1
License:	BSD-like
Group:		Applications/Networking
Source0:	http://dns.measurement-factory.com/tools/dnstop/src/%{name}-20060517.tar.gz
# Source0-md5:	42181157acfe8e51fd8948ad4de7506d
URL:		http://dns.measurement-factory.com/tools/dnstop/
BuildRequires:	libpcap-devel
BuildRequires:  ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dnstop is a libpcap application (ala tcpdump) that displays various
tables of DNS traffic on your network, including tables of source and
destination IP addresses, query types, top level domains and second
level domains.

%description -l pl
dnstop to aplikacja oparta na libpcap (podobnie jak tcpdump)
wy¶wietlaj±ca zestawienia ruchu DNS w sieci wraz z tabelami ¼ród³owych
i docelowych adresów IP, rodzajów zapytañ, domen g³ównych i drugiego
poziomu.

%prep
%setup -q 

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I/usr/include/ncurses"

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
