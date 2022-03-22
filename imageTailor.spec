Name:         imageTailor
Summary:      Cut out the ISO
License:      Mulan PSL v2
Group:        System/Management
Version:      1.0.3
Release:      1
BuildRoot:    %{_tmppath}/%{name}-%{version}
Source:       https://gitee.com/openeuler/imageTailor/repository/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:     dnf-utils tar python3 drpm genisoimage python3-kiwi kiwi-tools kiwi-systemdeps
%description
Dopralinux custom tool

%prep
%setup -c

%install
iso_arch=$(uname -m)
mkdir -p %{buildroot}/opt/imageTailor
cd %{name}
cp -a conf/${iso_arch}/* %{buildroot}/opt/imageTailor
cp -a conf/common/* %{buildroot}/opt/imageTailor
cp -a mkdliso %{buildroot}/opt/imageTailor

# for user install hook config
chmod 600 %{buildroot}/opt/imageTailor/custom/cfg_*/usr_install/hook/install_succ_hook/S00reboot
chmod 600 %{buildroot}/opt/imageTailor/custom/cfg_*/usr_install/hook/after_setup_os_hook/S00setcap
chmod 640 %{buildroot}/opt/imageTailor/custom/cfg_*/usr_install/all/addonscript/after_inssucc_hook/*

# for user config
chmod 640 %{buildroot}/opt/imageTailor/custom/cfg_*/usr_install/conf/*
chmod 640 %{buildroot}/opt/imageTailor/custom/cfg_*/cmd.conf
chmod 640 %{buildroot}/opt/imageTailor/custom/cfg_*/rpm.conf
chmod 600 %{buildroot}/opt/imageTailor/custom/cfg_*/security_s.conf
chmod 640 %{buildroot}/opt/imageTailor/custom/cfg_*/sys.conf

# for execute scripts
chmod 550 %{buildroot}/opt/imageTailor/kiwi/hook/config.sh
chmod 550 %{buildroot}/opt/imageTailor/kiwi/hook/images.sh
chmod 550 %{buildroot}/opt/imageTailor/mkdliso

cd -

%pre

%post

%preun

%postun


%files
%defattr(-,root,root)
%dir /opt/imageTailor
/opt/imageTailor/*

%clean
rm -rf $RPM_BUILD_ROOT/*
rm -rf %{_tmppath}/%{name}-%{version}
rm -rf $RPM_BUILD_DIR/%{name}-%{version}

%changelog
* Mon Mar 21 2022 xinsheng<xinsheng3@huawei.com> - 1.0.3-1
- ID:NA
- SUG:NA
- DESC:init openEuler file config

* Wed Mar 16 2022 xinsheng<xinsheng3@huawei.com> - 1.0.2-1
- ID:NA
- SUG:NA
- DESC:adapter keyword for openEuler

* Thu Mar 03 2022 xinsheng<xinsheng3@huawei.com> - 1.0.1-1
- ID:NA
- SUG:NA
- DESC:append arm ko for pxe

* Mon Feb 28 2022 xinsheng<xinsheng3@huawei.com> - 1.0.0-1
- ID:NA
- SUG:NA
- DESC:package init
