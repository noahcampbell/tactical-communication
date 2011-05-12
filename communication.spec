Name:           communication
Version:       	1.0 
Release:        6%{?dist}
Summary:       	Communication Utilities for Tactical.io 

Group:         	Tactical.io/Operations 
License:       	Proprietary 
URL:           	https://github.com/noahcampbell/tactical-communication 
Source0:       	communication-%{version}.tar.gz 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  procmail
Requires:       python >= 2.7
Requires:	procmail
Requires:	ripmime

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
%defattr(-,tacingress,tactical,-)
#%doc
%dir /var/lib/tactical-communication
%dir /var/tactical/activity
%dir /var/tactical/ingress/attachments
/var/lib/tactical-communication/get-tactical-ingress
/var/lib/tactical-communication/publish-attachments
/var/lib/tactical-communication/.procmailrc

%pre
#add the tactical group and tacingress user
getent group tactical >/dev/null || groupadd -r tactical
getent passwd tacingress >/dev/null || useradd -c "tacingress" -g tactical  -s /sbin/nologin \
  -s /sbin/nologin -r -d /var/lib/tactical-communication tacingress 2>/dev/null

%post
# Add alias to /etc/aliases and update the database
grep -q ^get: /etc/aliases || {
	echo "get: tacingress" >> /etc/aliases
	newaliases >/dev/null
}

%changelog
* Wed May 11 2011 Noah Campbell - 1.0-6
- Fix path in pm-get.rc

* Wed May 11 2011 Noah Campbell - 1.0-5
- Include ripmime dependency.
- Fix paths in .procmailrc

* Wed May 11 2011 Noah Campbell - 1.0-4
- Fixed %pre section

* Wed May 11 2011 Noah Campbell - 1.0-3
- Add publish-attachments

* Sun May 08 2011 Noah Campbell - 1.0-2
- Initial Version

