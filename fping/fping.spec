Name: fping
Version: 3.10
Release: 1%{?dist}
Summary: Scriptable, parallelized ping-like utility
Group: Applications/Internet
License: BSD with advertising
URL: http://fping.org/
Source0: %{name}-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
fping is a program to send ICMP echo probes to network hosts, similar to ping,
but much better performing when pinging multiple hosts.

%prep
%setup -q -n %{name}-%{version}

%build
%configure --enable-ipv4 --enable-ipv6
make CFLAGS="$RPM_OPT_FLAGS"

make clean
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR="$RPM_BUILD_ROOT" install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING README
%attr(4755,root,root) %{_sbindir}/fping
%attr(4755,root,root) %{_sbindir}/fping6
%{_mandir}/man8/*

%changelog
* Tue Jun 24 2014 Kodai Terashima <kodai.terashima@zabbix.com> - 3.10-1
- update to 3.10

* Thu Jul 6 2010 Kodai Terashima <kodai.terashima@zabbix.com> - 3.9-1
- Initial release for fping3
