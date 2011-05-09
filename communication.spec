Name:           communication
Version:       	1.0 
Release:        2%{?dist}
Summary:       	Communication Utilities for Tactical.io 

Group:         	Tactical.io/Operations 
License:       	Proprietary 
URL:           	https://github.com/noahcampbell/tactical-communication 
Source0:       	communication-%{version}.tar.gz 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  procmail
Requires:       python >= 2.7
Requires:	procmail

%description
Communication within tactical.io is a big part of the experience.  This package contains those key pieces.

%prep 
%setup -q -c comm


%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
#%doc
%dir %attr(-, tacingress, tacingress) /var/lib/tactical-communication
/var/lib/tactical-communication/get-tactical-ingress
/var/lib/tactical-communication/.procmailrc

%pre
getent group tactical >/dev/null || groupadd -r tactical
getent passwd tacingress >/dev/null || useradd -c "tacingress" -g tactical  -s /sbin/nologin \
  -s /sbin/nologin -r -d /var/lib/tactical-communication 2> /dev/null

%changelog
* Sun May 08 2011 Noah Campbell - 1.0-2
- rebuilt

