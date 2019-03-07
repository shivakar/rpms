Name:		vim
Version:	8.1.0996
Release:	1%{?dist}
Summary:	A version of VIM editor which includes recent enhancements

License:	Vim
URL:		https://www.vim.org
Source:		https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz

BuildRequires:	ruby ruby-devel
BuildRequires:	lua lua-devel luajit luajit-devel
BuildRequires:	ctags
BuildRequires:	git
BuildRequires:	python python-devel
BuildRequires:	tcl-devel
BuildRequires:	perl perl-devel
BuildRequires:	perl-ExtUtils-ParseXS perl-ExtUtils-XSpp perl-ExtUtils-CBuilder perl-ExtUtils-Embed

Obsoletes:	%{name} <= %{version}
Provides:	%{name} = %{version}
Conflicts:	%{name}-enhanced
Conflicts:	%{name}-common


# rpmbuild --target x86_64 -bb vim.spec

%description

VIM (VIsual editor iMproved) is an updated and improved version of the vi editor.

%prep
%setup -q

%build
%configure	--with-features=huge \
		--enable-multibyte \
		--enable-cscope \
		--enable-luainterp \
		--enable-perlinterp \
		--enable-pythoninterp \
		--enable-rubyinterp \
		--enable-tcpinterpa

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALLBIN="install -p -m0755" INSTALLMAN="install -p -m0644"

%clean
rm -rf %{buildroot}

%files
%{_datadir}/*
%{_bindir}/*
%doc %{_mandir}/*

%changelog

* Wed Mar 06 2019 Shivakar Vulli <svulli@shivakar.com>
- vim 8.1.0996

