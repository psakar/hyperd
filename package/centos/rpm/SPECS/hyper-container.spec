Summary:            Hyper Container is a VM based docker runtime
Name:               hyper-container
Version:            0.8.1
Release:            1%{?dist}
License:            Apache License, Version 2.0
Group:              System Environment/Base
# The source for this package was pulled from upstream's git repo. Use the
# following commands to generate the tarball:
#  git archive --format=tar.gz master > hyperd-%{version}.tar.gz
Source0:            hyperd-%{version}.tar.gz
URL:                https://hyper.sh/
ExclusiveArch:      x86_64
Requires:           device-mapper,sqlite
BuildRequires:      device-mapper-devel,pcre-devel,libsepol-devel,libselinux-devel
#BuildRequires:      systemd-devel
BuildRequires:      sqlite-devel
#CentOS 7 does not have xen included
#BuildRequires:      libuuid-devel,xen-devel

%description
Hyper is a VM based docker engine, it start a container image in
VM without a full guest OS

%prep
mkdir -p %{_builddir}/src/github.com/hyperhq/hyperd
tar -C %{_builddir}/src/github.com/hyperhq/hyperd -xvf %SOURCE0

%build
cd %{_builddir}/src/github.com/hyperhq/hyperd
export GOPATH=%{_builddir}
./autogen.sh
./configure
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}/lib/systemd/system/
cp %{_builddir}/src/github.com/hyperhq/hyperd/{hyperctl,hyperd,vmlogd} %{buildroot}%{_bindir}
cp -a %{_builddir}/src/github.com/hyperhq/hyperd/package/dist/etc/hyper %{buildroot}%{_sysconfdir}
cp -a %{_builddir}/src/github.com/hyperhq/hyperd/package/dist/lib/systemd/system/hyperd.service %{buildroot}/lib/systemd/system/hyperd.service
cp -a %{_builddir}/src/github.com/hyperhq/hyperd/package/dist/lib/systemd/system/hyper-vmlogd.service %{buildroot}/lib/systemd/system/hyper-vmlogd.service

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_sysconfdir}/*
/lib/systemd/system/hyperd.service
/lib/systemd/system/hyper-vmlogd.service

%changelog
* Mon May 8 2017 Hyper Dev Team <dev@hyper.sh> - 0.8.1-1
- update source to 0.8.1
* Mon Mar 20 2017 Hyper Dev Team <dev@hyper.sh> - 0.8.0-1
- update source to 0.8.0
* Fri Oct 28 2016 Hyper Dev Team <dev@hyper.sh> - 0.7.0-1
- update source to 0.7.0
* Mon Aug 29 2016 Hyper Dev Team <dev@hyper.sh> - 0.6.2-1
- update source to 0.6.2
* Thu Apr 28 2016 Hyper Dev Team <dev@hyper.sh> - 0.6-1
- update source to 0.6
- rename package
* Sat Jan 30 2016 Xu Wang <xu@hyper.sh> - 0.5-1
- update source to 0.5
- introduce libvirt dependency
* Wed Dec 2 2015 Xu Wang <xu@hyper.sh> - 0.4-2
- add hyperstart dependency
- add systemd service config
* Sat Nov 21 2015 Xu Wang <xu@hyper.sh> - 0.4-1
- Initial rpm packaging
