Summary: Gluster Filesystem from the CentOS Storage SIG repo configs
Name: centos-release-gluster
Epoch: 10
Version: 1
Release: 2%{?dist}
License: GPL
Group: System Environment/Base
Source0: CentOS-Gluster.repo
URL: http://wiki.centos.org/SpecialInterestGroup/Storage
BuildArch: noarch

Provides: centos-release-gluster
Requires: centos-release

BuildRoot: %{_tmppath}/%{name}-root

%description
yum Configs and basic docs for Gluster FS as delivered via the CentOS Storage SIG.

%prep
%setup -q -n %{name} -T -c

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc
mkdir -p -m 755 $RPM_BUILD_ROOT/etc/yum.repos.d
mkdir -p -m 755 $RPM_BUILD_ROOT/%{_bindir}
install -m 644 %SOURCE0 $RPM_BUILD_ROOT/etc/yum.repos.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config(noreplace) /etc/yum.repos.d/*

%changelog
* Mon Nov 10 2014 Karanbir Singh <kbsingh@centos.org> - 1-2
* Fixed the testing repo http path in the repo file ( lalatendu ) 

* Wed Oct 15 2014 Karanbir Singh <kbsingh@centos.org> - 1-1
- Basic setup with the repo files so we can start testing
