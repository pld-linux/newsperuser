Summary:	News client.
Summary(pl):	Klient news.
Name:		news-peruser
Version:	4.0beta33
Release:	1
Group:		Applications/Internet
######		Unknown group!
Group(pl):	Aplikacje/Internet
License:	GPL
Vendor:		PLD
Source0:	http://peruser.netpedia.net/%{name}-%{version}.tar.gz
URL:		http://peruser.netpedia.net 
BuildArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

install -d $RPM_BUILD_ROOT%{_prefix}/{bin,share/%{name},share/doc}
install -d $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version} 


%{__make} install 

gzip -9nf AUTHORS ChangeLog HACKING INSTALL NEWS README TODO 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_datadir}/%{name}/*
%doc AUT*gz Chang*gz HACK*gz INSTA*gz NEW*gz READ*gz TO*gz
