Summary:	News client
Summary(pl):	Klient news
Name:		news-peruser
Version:	4.0beta33
Release:	2
Group:		X11/Applications/Networking
License:	GPL
Source0:	http://peruser.netpedia.net/%{name}-%{version}.tar.gz
URL:		http://peruser.netpedia.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
GNOME news client.

%description -l pl
Klient news dla GNOME.

%prep
%setup -q

%build
./configure --prefix=$RPM_BUILD_ROOT%{_prefix} --exec-prefix=$RPM_BUILD_ROOT%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

%{__make} install 

gzip -9nf AUTHORS ChangeLog HACKING INSTALL NEWS README TODO 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%doc AUT*gz Chang*gz HACK*gz INSTA*gz NEW*gz READ*gz TO*gz
