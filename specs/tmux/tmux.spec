Name:		tmux
Version:	2.8
Release:	1%{?dist}
Summary:	A terminal multiplexer

Group:		Applications/System
License:	BSD
URL:		http://github.com/tmux/tmux
Source:		https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	ncurses-devel
BuildRequires:	libevent-devel

# rpmbuild --target x86_64 -bb tmux.spec

%description
tmux is a "terminal multiplexer."  It enables a number of terminals (or windows) to be accessed and controlled from a single terminal.  tmux is intended to be a simple, modern, BSD-licensed alternative to programs such as GNU Screen.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALLBIN="install -p -m0755" INSTALLMAN="install -p -m0644"

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/tmux.1.*
%attr(2755, root, root) %{_bindir}/tmux

%changelog

* Wed Mar 06 2019 Shivakar Vulli <svulli@shivakar.com>
- tmux 2.8

