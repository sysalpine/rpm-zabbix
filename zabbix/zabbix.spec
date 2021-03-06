Name:     zabbix
Version:  4.2.4
Release:  1%{?dist}
Epoch:    1
Summary:  The Enterprise-class open source monitoring solution
Group:    Applications/Internet
License:  GPLv2+
URL:      http://www.zabbix.com/
Source0:  %{name}-%{version}%{?alphatag}.tar.gz
Source1:  zabbix-logrotate.in
Source2:  zabbix-agent.service
Source3:  zabbix-server.service
Source4:  zabbix-proxy.service
Source5:  zabbix-tmpfiles.conf
Patch0:   config.patch

Buildroot: %{_tmppath}/zabbix-%{?epoch:%{epoch}:}%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  make
BuildRequires:  mysql-devel
BuildRequires:  postgresql-devel
BuildRequires:  net-snmp-devel
%if 0%{?rhel} || 0%{?fedora}
BuildRequires:  openldap-devel
%else
BuildRequires:  openldap2-devel
%endif
BuildRequires:  gnutls-devel
BuildRequires:  sqlite-devel
BuildRequires:  unixODBC-devel
BuildRequires:  curl-devel >= 7.13.1
BuildRequires:  OpenIPMI-devel >= 2
BuildRequires:  libssh2-devel >= 1.0.0
BuildRequires:  libxml2-devel
BuildRequires:  pcre-devel
BuildRequires:  libevent-devel
%if 0%{?rhel} || 0%{?fedora}
BuildRequires:  openssl-devel >= 1.0.1
%else
BuildRequires:  libopenssl-devel
%endif
BuildRequires:  systemd

%description
Zabbix is the ultimate enterprise-level software designed for
real-time monitoring of millions of metrics collected from tens of
thousands of servers, virtual machines and network devices.

%package agent
Summary:          Zabbix Agent
Group:            Applications/Internet
Requires:         logrotate
Requires(pre):    /usr/sbin/useradd
Requires(post):   systemd
Requires(preun):  systemd
Requires(preun):  systemd

%description agent
Zabbix agent to be installed on monitored systems.

%package get
Summary:          Zabbix Get
Group:            Applications/Internet

%description get
Zabbix get command line utility

%package sender
Summary:          Zabbix Sender
Group:            Applications/Internet

%description sender
Zabbix sender command line utility

%package proxy-mysql
Summary:          Zabbix proxy for MySQL or MariaDB database
Group:            Applications/Internet
Requires:         fping
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
Provides:         zabbix-proxy = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:         zabbix-proxy-implementation = %{?epoch:%{epoch}:}%{version}-%{release}

%description proxy-mysql
Zabbix proxy with MySQL or MariaDB database support.

%package proxy-pgsql
Summary:          Zabbix proxy for PostgreSQL database
Group:            Applications/Internet
Requires:         fping
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
Provides:         zabbix-proxy = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:         zabbix-proxy-implementation = %{?epoch:%{epoch}:}%{version}-%{release}

%description proxy-pgsql
Zabbix proxy with PostgreSQL database support.

%package proxy-sqlite3
Summary:          Zabbix proxy for SQLite3 database
Group:            Applications/Internet
Requires:         fping
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
Provides:         zabbix-proxy = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:         zabbix-proxy-implementation = %{?epoch:%{epoch}:}%{version}-%{release}

%description proxy-sqlite3
Zabbix proxy with SQLite3 database support.

%package server-mysql
Summary:          Zabbix server for MySQL or MariaDB database
Group:            Applications/Internet
Requires:         fping
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
Provides:         zabbix-server = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:         zabbix-server-implementation = %{?epoch:%{epoch}:}%{version}-%{release}

%description server-mysql
Zabbix server with MySQL or MariaDB database support.

%package server-pgsql
Summary:          Zabbix server for PostgresSQL database
Group:            Applications/Internet
Requires:         fping
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
Provides:         zabbix-server = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:         zabbix-server-implementation = %{?epoch:%{epoch}:}%{version}-%{release}

%description server-pgsql
Zabbix server with PostgresSQL database support.

%package web
Summary:          Zabbix web frontend common package
Group:            Application/Internet
BuildArch:        noarch
Requires:         php >= 5.4
Requires:         php-gd
Requires:         php-bcmath
Requires:         php-mbstring
Requires:         php-xml
Requires:         php-ldap
Requires:         dejavu-sans-fonts
Requires:         zabbix-web-database = %{?epoch:%{epoch}:}%{version}-%{release}
Requires(post):   %{_sbindir}/update-alternatives
Requires(preun):  %{_sbindir}/update-alternatives

%description web
Zabbix web frontend common package

%package web-mysql
Summary:          Zabbix web frontend for MySQL
Group:            Applications/Internet
BuildArch:        noarch
%if 0%{?rhel} || 0%{?fedora}
Requires:         php-mysqlnd
%else
#suse leap
Requires:         php7-mysql
%endif
Requires:         zabbix-web = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:         zabbix-web-database = %{?epoch:%{epoch}:}%{version}-%{release}

%description web-mysql
Zabbix web frontend for MySQL

%package web-pgsql
Summary:          Zabbix web frontend for PostgreSQL
Group:            Applications/Internet
BuildArch:        noarch
%if 0%{?rhel} || 0%{?fedora}
Requires:         php-pgsql
%else
#suse leap
Requires:         php7-pgsql
%endif
Requires:         zabbix-web = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:         zabbix-web-database = %{?epoch:%{epoch}:}%{version}-%{release}

%description web-pgsql
Zabbix web frontend for PostgreSQL

%package web-japanese
Summary:          Japanese font settings for frontend
Group:            Applications/Internet
BuildArch:        noarch
Requires:         vlgothic-p-fonts
Requires:         zabbix-web = %{?epoch:%{epoch}:}%{version}-%{release}
Requires(post):   %{_sbindir}/update-alternatives
Requires(preun):  %{_sbindir}/update-alternatives

%description web-japanese
Japanese font configuration for Zabbix web frontend

%prep
%setup0 -q -n %{name}-%{version}%{?alphatag}
%patch0 -p1

## remove font file
#rm -f frontends/php/fonts/DejaVuSans.ttf

# remove .htaccess files
rm -f frontends/php/app/.htaccess
rm -f frontends/php/conf/.htaccess
rm -f frontends/php/include/.htaccess
rm -f frontends/php/local/.htaccess

# remove translation source files and scripts
find frontends/php/locale -name '*.po' | xargs rm -f
find frontends/php/locale -name '*.sh' | xargs rm -f

# traceroute command path for global script
sed -i -e 's|/usr/bin/traceroute|/bin/traceroute|' database/mysql/data.sql
sed -i -e 's|/usr/bin/traceroute|/bin/traceroute|' database/postgresql/data.sql
sed -i -e 's|/usr/bin/traceroute|/bin/traceroute|' database/sqlite3/data.sql

# copy sql files for servers
cat database/mysql/schema.sql > database/mysql/create.sql
cat database/mysql/images.sql >> database/mysql/create.sql
cat database/mysql/data.sql >> database/mysql/create.sql
gzip database/mysql/create.sql

cat database/postgresql/schema.sql > database/postgresql/create.sql
cat database/postgresql/images.sql >> database/postgresql/create.sql
cat database/postgresql/data.sql >> database/postgresql/create.sql
gzip database/postgresql/create.sql
gzip database/postgresql/timescaledb.sql

# sql files for proxyes
gzip database/mysql/schema.sql
gzip database/postgresql/schema.sql
gzip database/sqlite3/schema.sql


%build

build_flags="
  --enable-dependency-tracking
  --sysconfdir=/etc/zabbix
  --libdir=%{_libdir}/zabbix
  --enable-agent
  --enable-proxy
  --enable-ipv6
  --with-net-snmp
  --with-ldap
  --with-libcurl
  --with-openipmi
  --with-unixodbc
  --with-ssh2
  --with-libxml2
  --with-libevent
  --with-libpcre
  --with-openssl
"

%configure $build_flags --with-sqlite3
make %{?_smp_mflags}
mv src/zabbix_proxy/zabbix_proxy src/zabbix_proxy/zabbix_proxy_sqlite3

build_flags="$build_flags --enable-server"

%configure $build_flags --with-mysql
make %{?_smp_mflags}
mv src/zabbix_server/zabbix_server src/zabbix_server/zabbix_server_mysql
mv src/zabbix_proxy/zabbix_proxy src/zabbix_proxy/zabbix_proxy_mysql

%configure $build_flags --with-postgresql
make %{?_smp_mflags}
mv src/zabbix_server/zabbix_server src/zabbix_server/zabbix_server_pgsql
mv src/zabbix_proxy/zabbix_proxy src/zabbix_proxy/zabbix_proxy_pgsql

touch src/zabbix_server/zabbix_server
touch src/zabbix_proxy/zabbix_proxy


%install

rm -rf $RPM_BUILD_ROOT

# install
make DESTDIR=$RPM_BUILD_ROOT install

# install necessary directories
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/zabbix
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/run/zabbix

# install server and proxy binaries
install -m 0755 -p src/zabbix_server/zabbix_server_* $RPM_BUILD_ROOT%{_sbindir}/
rm $RPM_BUILD_ROOT%{_sbindir}/zabbix_server
install -m 0755 -p src/zabbix_proxy/zabbix_proxy_* $RPM_BUILD_ROOT%{_sbindir}/
rm $RPM_BUILD_ROOT%{_sbindir}/zabbix_proxy

# install scripts and modules directories
mkdir -p $RPM_BUILD_ROOT/usr/lib/zabbix
mv $RPM_BUILD_ROOT%{_datadir}/zabbix/alertscripts $RPM_BUILD_ROOT/usr/lib/zabbix
mv $RPM_BUILD_ROOT%{_datadir}/zabbix/externalscripts $RPM_BUILD_ROOT/usr/lib/zabbix

# install frontend files
find frontends/php -name '*.orig' | xargs rm -f
cp -a frontends/php/* $RPM_BUILD_ROOT%{_datadir}/zabbix

# install frontend configuration files
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/web
touch $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/web/zabbix.conf.php
mv $RPM_BUILD_ROOT%{_datadir}/zabbix/conf/maintenance.inc.php $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/web/

# install configuration files
mv $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/zabbix_agentd.conf.d $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/zabbix_agentd.d
mv $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/zabbix_proxy.conf.d $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/zabbix_proxy.d
mv $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/zabbix_server.conf.d $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/zabbix_server.d

install -dm 755 $RPM_BUILD_ROOT%{_docdir}/zabbix-agent-%{version}

install -m 0644 conf/zabbix_agentd/userparameter_mysql.conf $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/zabbix_agentd.d

cat conf/zabbix_agentd.conf | sed \
  -e '/^# PidFile=/a \\nPidFile=%{_localstatedir}/run/zabbix/zabbix_agentd.pid' \
  -e 's|^LogFile=.*|LogFile=%{_localstatedir}/log/zabbix/zabbix_agentd.log|g' \
  -e '/^# LogFileSize=.*/a \\nLogFileSize=0' \
  -e '/^# Include=$/a \\nInclude=%{_sysconfdir}/zabbix/zabbix_agentd.d/*.conf' \
  > $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/zabbix_agentd.conf

cat conf/zabbix_server.conf | sed \
  -e '/^# PidFile=/a \\nPidFile=%{_localstatedir}/run/zabbix/zabbix_server.pid' \
  -e 's|^LogFile=.*|LogFile=%{_localstatedir}/log/zabbix/zabbix_server.log|g' \
  -e '/^# LogFileSize=/a \\nLogFileSize=0' \
  -e '/^# AlertScriptsPath=/a \\nAlertScriptsPath=/usr/lib/zabbix/alertscripts' \
  -e '/^# ExternalScripts=/a \\nExternalScripts=/usr/lib/zabbix/externalscripts' \
  -e 's|^DBUser=root|DBUser=zabbix|g' \
  -e '/^# SNMPTrapperFile=.*/a \\nSNMPTrapperFile=/var/log/snmptrap/snmptrap.log' \
  -e '/^# SocketDir=.*/a \\nSocketDir=/var/run/zabbix' \
  > $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/zabbix_server.conf

cat conf/zabbix_proxy.conf | sed \
  -e '/^# PidFile=/a \\nPidFile=%{_localstatedir}/run/zabbix/zabbix_proxy.pid' \
  -e 's|^LogFile=.*|LogFile=%{_localstatedir}/log/zabbix/zabbix_proxy.log|g' \
  -e '/^# LogFileSize=/a \\nLogFileSize=0' \
  -e '/^# ExternalScripts=/a \\nExternalScripts=/usr/lib/zabbix/externalscripts' \
  -e 's|^DBUser=root|DBUser=zabbix|g' \
  -e '/^# SNMPTrapperFile=.*/a \\nSNMPTrapperFile=/var/log/snmptrap/snmptrap.log' \
  -e '/^# SocketDir=.*/a \\nSocketDir=/var/run/zabbix' \
  > $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/zabbix_proxy.conf

# install logrotate configuration files
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
cat %{SOURCE1} | sed \
  -e 's|COMPONENT|server|g' \
  > $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/zabbix-server
cat %{SOURCE1} | sed \
  -e 's|COMPONENT|agentd|g' \
  > $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/zabbix-agent
cat %{SOURCE1} | sed \
  -e 's|COMPONENT|proxy|g' \
  > $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/zabbix-proxy

# install startup scripts
install -Dm 0644 -p %{SOURCE2} $RPM_BUILD_ROOT%{_unitdir}/zabbix-agent.service
install -Dm 0644 -p %{SOURCE3} $RPM_BUILD_ROOT%{_unitdir}/zabbix-server.service
install -Dm 0644 -p %{SOURCE4} $RPM_BUILD_ROOT%{_unitdir}/zabbix-proxy.service

# install systemd-tmpfiles conf
install -Dm 0644 -p %{SOURCE5} $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d/zabbix-agent.conf
install -Dm 0644 -p %{SOURCE5} $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d/zabbix-server.conf
install -Dm 0644 -p %{SOURCE5} $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d/zabbix-proxy.conf


%clean
rm -rf $RPM_BUILD_ROOT


%pre agent
getent group zabbix > /dev/null || groupadd -r zabbix
getent passwd zabbix > /dev/null || \
  useradd -r -g zabbix -d %{_localstatedir}/lib/zabbix -s /sbin/nologin \
  -c "Zabbix Monitoring System" zabbix
:

%post agent
%systemd_post zabbix-agent.service

%pre proxy-mysql
getent group zabbix > /dev/null || groupadd -r zabbix
getent passwd zabbix > /dev/null || \
  useradd -r -g zabbix -d %{_localstatedir}/lib/zabbix -s /sbin/nologin \
  -c "Zabbix Monitoring System" zabbix
:

%pre proxy-pgsql
getent group zabbix > /dev/null || groupadd -r zabbix
getent passwd zabbix > /dev/null || \
  useradd -r -g zabbix -d %{_localstatedir}/lib/zabbix -s /sbin/nologin \
  -c "Zabbix Monitoring System" zabbix
:

%pre proxy-sqlite3
getent group zabbix > /dev/null || groupadd -r zabbix
getent passwd zabbix > /dev/null || \
  useradd -r -g zabbix -d %{_localstatedir}/lib/zabbix -s /sbin/nologin \
  -c "Zabbix Monitoring System" zabbix
:

%pre server-mysql
getent group zabbix > /dev/null || groupadd -r zabbix
getent passwd zabbix > /dev/null || \
  useradd -r -g zabbix -d %{_localstatedir}/lib/zabbix -s /sbin/nologin \
  -c "Zabbix Monitoring System" zabbix
:

%pre server-pgsql
getent group zabbix > /dev/null || groupadd -r zabbix
getent passwd zabbix > /dev/null || \
  useradd -r -g zabbix -d %{_localstatedir}/lib/zabbix -s /sbin/nologin \
  -c "Zabbix Monitoring System" zabbix
:


%post proxy-mysql
%systemd_post zabbix-proxy.service
/usr/sbin/update-alternatives --install %{_sbindir}/zabbix_proxy zabbix-proxy %{_sbindir}/zabbix_proxy_mysql 10
:

%post proxy-pgsql
%systemd_post zabbix-proxy.service
/usr/sbin/update-alternatives --install %{_sbindir}/zabbix_proxy zabbix-proxy %{_sbindir}/zabbix_proxy_pgsql 10
:

%post proxy-sqlite3
%systemd_post zabbix-proxy.service
/usr/sbin/update-alternatives --install %{_sbindir}/zabbix_proxy zabbix-proxy %{_sbindir}/zabbix_proxy_sqlite3 10
:

%post server-mysql
%systemd_post zabbix-server.service
/usr/sbin/update-alternatives --install %{_sbindir}/zabbix_server zabbix-server %{_sbindir}/zabbix_server_mysql 10
:

%post server-pgsql
%systemd_post zabbix-server.service
/usr/sbin/update-alternatives --install %{_sbindir}/zabbix_server zabbix-server %{_sbindir}/zabbix_server_pgsql 10
:

%post web
/usr/sbin/update-alternatives --install %{_datadir}/zabbix/fonts/graphfont.ttf zabbix-web-font %{_datadir}/fonts/dejavu/DejaVuSans.ttf 10
:

%post web-japanese
/usr/sbin/update-alternatives --install %{_datadir}/zabbix/fonts/graphfont.ttf zabbix-web-font %{_datadir}/fonts/vlgothic/VL-PGothic-Regular.ttf 20
:

%preun agent
if [ "$1" = 0 ]; then
%systemd_preun zabbix-agent.service
fi
:

%preun proxy-mysql
%systemd_preun zabbix-proxy.service
if [ "$1" = 0 ]; then
  /usr/sbin/update-alternatives --remove zabbix-proxy %{_sbindir}/zabbix_proxy_mysql
fi
:

%preun proxy-pgsql
%systemd_preun zabbix-proxy.service
if [ "$1" = 0 ]; then
  /usr/sbin/update-alternatives --remove zabbix-proxy %{_sbindir}/zabbix_proxy_pgsql
fi
:

%preun proxy-sqlite3
%systemd_preun zabbix-proxy.service
if [ "$1" = 0 ]; then
  /usr/sbin/update-alternatives --remove zabbix-proxy %{_sbindir}/zabbix_proxy_sqlite3
fi
:

%systemd_preun zabbix-server.service
%preun server-mysql
if [ "$1" = 0 ]; then
  /usr/sbin/update-alternatives --remove zabbix-server %{_sbindir}/zabbix_server_mysql
fi
:

%preun server-pgsql
%systemd_preun zabbix-server.service
if [ "$1" = 0 ]; then
  /usr/sbin/update-alternatives --remove zabbix-server %{_sbindir}/zabbix_server_pgsql
fi
:

%preun web
if [ "$1" = 0 ]; then
  /usr/sbin/update-alternatives --remove zabbix-web-font %{_datadir}/fonts/dejavu/DejaVuSans.ttf
fi
:

%preun web-japanese
if [ "$1" = 0 ]; then
  /usr/sbin/update-alternatives --remove zabbix-web-font %{_datadir}/fonts/vlgothic/VL-PGothic-Regular.ttf
fi
:

%postun agent
%systemd_postun_with_restart zabbix-agent.service

%postun proxy-mysql
%systemd_postun_with_restart zabbix-proxy.service

%postun proxy-pgsql
%systemd_postun_with_restart zabbix-proxy.service

%postun proxy-sqlite3
%systemd_postun_with_restart zabbix-proxy.service

%postun server-mysql
%systemd_postun_with_restart zabbix-server.service

%postun server-pgsql
%systemd_postun_with_restart zabbix-server.service


%files agent
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%config(noreplace) %{_sysconfdir}/zabbix/zabbix_agentd.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/zabbix-agent
%dir %{_sysconfdir}/zabbix/zabbix_agentd.d
%config(noreplace) %{_sysconfdir}/zabbix/zabbix_agentd.d/userparameter_mysql.conf
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/log/zabbix
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/run/zabbix
%{_sbindir}/zabbix_agentd
%{_mandir}/man8/zabbix_agentd.8*
%{_unitdir}/zabbix-agent.service
%{_prefix}/lib/tmpfiles.d/zabbix-agent.conf


%files get
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/zabbix_get
%{_mandir}/man1/zabbix_get.1*

%files sender
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/zabbix_sender
%{_mandir}/man1/zabbix_sender.1*

%files proxy-mysql
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc database/mysql/schema.sql.gz
%attr(0640,root,zabbix) %config(noreplace) %{_sysconfdir}/zabbix/zabbix_proxy.conf
%dir /usr/lib/zabbix/externalscripts
%config(noreplace) %{_sysconfdir}/logrotate.d/zabbix-proxy
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/log/zabbix
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/run/zabbix
%{_mandir}/man8/zabbix_proxy.8*
%{_unitdir}/zabbix-proxy.service
%{_prefix}/lib/tmpfiles.d/zabbix-proxy.conf
%{_sbindir}/zabbix_proxy_mysql

%files proxy-pgsql
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc database/postgresql/schema.sql.gz
%attr(0640,root,zabbix) %config(noreplace) %{_sysconfdir}/zabbix/zabbix_proxy.conf
%dir /usr/lib/zabbix/externalscripts
%config(noreplace) %{_sysconfdir}/logrotate.d/zabbix-proxy
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/log/zabbix
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/run/zabbix
%{_mandir}/man8/zabbix_proxy.8*
%{_unitdir}/zabbix-proxy.service
%{_prefix}/lib/tmpfiles.d/zabbix-proxy.conf
%{_sbindir}/zabbix_proxy_pgsql

%files proxy-sqlite3
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc database/sqlite3/schema.sql.gz
%attr(0640,root,zabbix) %config(noreplace) %{_sysconfdir}/zabbix/zabbix_proxy.conf
%dir /usr/lib/zabbix/externalscripts
%config(noreplace) %{_sysconfdir}/logrotate.d/zabbix-proxy
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/log/zabbix
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/run/zabbix
%{_mandir}/man8/zabbix_proxy.8*
%{_unitdir}/zabbix-proxy.service
%{_prefix}/lib/tmpfiles.d/zabbix-proxy.conf
%{_sbindir}/zabbix_proxy_sqlite3

%files server-mysql
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc database/mysql/create.sql.gz
%attr(0640,root,zabbix) %config(noreplace) %{_sysconfdir}/zabbix/zabbix_server.conf
%dir /usr/lib/zabbix/alertscripts
%dir /usr/lib/zabbix/externalscripts
%config(noreplace) %{_sysconfdir}/logrotate.d/zabbix-server
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/log/zabbix
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/run/zabbix
%{_mandir}/man8/zabbix_server.8*
%{_unitdir}/zabbix-server.service
%{_prefix}/lib/tmpfiles.d/zabbix-server.conf
%{_sbindir}/zabbix_server_mysql

%files server-pgsql
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc database/postgresql/create.sql.gz
%doc database/postgresql/timescaledb.sql.gz
%attr(0640,root,zabbix) %config(noreplace) %{_sysconfdir}/zabbix/zabbix_server.conf
%dir /usr/lib/zabbix/alertscripts
%dir /usr/lib/zabbix/externalscripts
%config(noreplace) %{_sysconfdir}/logrotate.d/zabbix-server
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/log/zabbix
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/run/zabbix
%{_mandir}/man8/zabbix_server.8*
%{_unitdir}/zabbix-server.service
%{_prefix}/lib/tmpfiles.d/zabbix-server.conf
%{_sbindir}/zabbix_server_pgsql

%files web
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%dir %attr(0750,apache,apache) %{_sysconfdir}/zabbix/web
%ghost %attr(0644,apache,apache) %config(noreplace) %{_sysconfdir}/zabbix/web/zabbix.conf.php
%config(noreplace) %{_sysconfdir}/zabbix/web/maintenance.inc.php
%{_datadir}/zabbix

%files web-mysql
%defattr(-,root,root,-)

%files web-pgsql
%defattr(-,root,root,-)

%files web-japanese
%defattr(-,root,root,-)


%changelog
* Mon Jun 10 2019 Paul Trunk <ptrunk@sysalpine.com> - 4.2.3-1
- Bump zabbix version to 4.2.3

* Mon Jun  3 2019 Paul Trunk <ptrunk@sysalpine.com> - 4.2.1-5
- Add Epoch tag

* Mon May 13 2019 Paul Trunk <ptrunk@sysalpine.com> - 4.2.1-4
- Fix php mysql and pgsql requirements

* Thu May  9 2019 Paul Trunk <ptrunk@sysalpine.com> - 4.2.1-3
- Remove Java Gateway

* Tue May  7 2019 Paul Trunk <ptrunk@sysalpine.com> - 4.2.1-2
- Fix tls for fedora and suse

* Sat May  4 2019 Paul Trunk <ptrunk@sysalpine.com> - 4.2.1-1
- Initial packages

