Summary: News client.
Summary(pl): Klient news.
Name: news-peruser
Version: 4.0beta33
Release: 1
Group: Applications/Internet
Group(pl): Aplikacje/Internet
Copyright: GPL
Vendor: PLD
Distribution: PLD
Source: http://peruser.netpedia.net/%{name}-%{version}.tar.gz 
URL: http://peruser.netpedia.net 
BuildArch: i386
BuildRoot: /tmp/%{name}-%{version}-root

%description
GNOME news client.

%description -l pl
Klient news dla GNOME.


%prep
%setup
%build

./configure --prefix=$RPM_BUILD_ROOT/usr --exec-prefix=$RPM_BUILD_ROOT/usr  
make


%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/{bin,share/%{name},share/doc} 
install -d $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version} 


make install 

gzip -9nf AUTHORS ChangeLog HACKING INSTALL NEWS README TODO 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/bin/*
%attr(644,root,root) /usr/share/%{name}/*
%doc AUT*gz Chang*gz HACK*gz INSTA*gz NEW*gz READ*gz TO*gz
