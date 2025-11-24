%global package_speccommit affe52814f2f268d23b7500a51e17dee54082705
%global package_srccommit v24.1.0
Name:           gpumon
Version: 24.1.0
Release: 71%{?xsrel}%{?dist}
Summary:        RRDD GPU metrics plugin
Group:          System/Hypervisor
License:        ISC
URL:            https://github.com/xenserver/gpumon
Source0: gpumon-24.1.0.tar.gz
Source1: xcp-rrdd-gpumon.service
BuildRoot:      %{_tmppath}/%{name}-%{version}-root
BuildRequires:  gdk-devel
BuildRequires:  xs-opam-repo
BuildRequires:  xcp-rrdd-devel
%{?systemd_requires}

%description
This package contains a plugin registering to the RRD daemon and exposing GPU
metrics.

%prep
%autosetup -p1

%build
DESTDIR=%{buildroot} %{__make}

%check
%{__make} test

%install
DESTDIR=%{buildroot} %{__make} install
%{__install} -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/xcp-rrdd-gpumon.service

%post
%systemd_post xcp-rrdd-gpumon.service

%preun
%systemd_preun xcp-rrdd-gpumon.service

%postun
%systemd_postun xcp-rrdd-gpumon.service

%files
/opt/xensource/libexec/xcp-rrdd-plugins/xcp-rrdd-gpumon
%{_unitdir}/xcp-rrdd-gpumon.service

%changelog
* Tue Oct 14 2025 Gabriel Buica <danutgabriel.buica@cloud.com> - 24.1.0-71
- Bump release and rebuild

* Tue Sep 30 2025 Gabriel Buica <danutgabriel.buica@cloud.com> - 24.1.0-70
- Bump release and rebuild

* Wed Sep 24 2025 Gabriel Buica <danutgabriel.buica@cloud.com> - 24.1.0-69
- Bump release and rebuild

* Tue Sep 02 2025 Gabriel Buica <danutgabriel.buica@cloud.com> - 24.1.0-68
- Bump release and rebuild

* Thu Aug 21 2025 Gabriel Buica <danutgabriel.buica@cloud.com> - 24.1.0-67
- Bump release and rebuild

* Wed Aug 06 2025 Gabriel Buica <danutgabriel.buica@cloud.com> - 24.1.0-66
- Bump release and rebuild

* Wed Jul 23 2025 Gabriel Buica <danutgabriel.buica@cloud.com> - 24.1.0-65
- Bump release and rebuild

* Wed Jul 16 2025 Rob Hoes <rob.hoes@citrix.com> - 24.1.0-64
- Bump release and rebuild

* Sun Jul 13 2025 Bengang Yuan <bengang.yuan@cloud.com> - 24.1.0-63
- Bump release and rebuild

* Sun Jul 06 2025 Bengang Yuan <bengang.yuan@cloud.com> - 24.1.0-62
- Bump release and rebuild

* Wed Jun 25 2025 Bengang Yuan <bengang.yuan@cloud.com> - 24.1.0-61
- Bump release and rebuild

* Thu Jun 12 2025 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 24.1.0-60
- Bump release and rebuild

* Wed Jun 11 2025 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 24.1.0-59
- Bump release and rebuild

* Tue Jun 10 2025 Bengang Yuan <bengang.yuan@cloud.com> - 24.1.0-58
- Bump release and rebuild

* Mon Jun 09 2025 Bengang Yuan <bengang.yuan@cloud.com> - 24.1.0-57
- Bump release and rebuild

* Fri Jun 06 2025 Bengang Yuan <bengang.yuan@cloud.com> - 24.1.0-56
- Bump release and rebuild

* Fri May 23 2025 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 24.1.0-55
- Bump release and rebuild

* Fri May 23 2025 Bengang Yuan <bengang.yuan@cloud.com> - 24.1.0-54
- Bump release and rebuild

* Thu May 15 2025 Bengang Yuan <bengang.yuan@cloud.com> - 24.1.0-53
- Bump release and rebuild

* Fri May 09 2025 Bengang Yuan <bengang.yuan@cloud.com> - 24.1.0-52
- Bump release and rebuild

* Thu Apr 24 2025 Bengang Yuan <bengang.yuan@cloud.com> - 24.1.0-51
- Bump release and rebuild

* Tue Apr 15 2025 Vincent Liu <shuntian.liu2@cloud.com> - 24.1.0-50
- Bump release and rebuild

* Tue Apr 08 2025 Vincent Liu <shuntian.liu2@cloud.com> - 24.1.0-49
- Bump release and rebuild

* Tue Mar 18 2025 Vincent Liu <shuntian.liu2@cloud.com> - 24.1.0-48
- Bump release and rebuild

* Mon Mar 17 2025 Vincent Liu <shuntian.liu2@cloud.com> - 24.1.0-47
- Bump release and rebuild

* Tue Mar 11 2025 Vincent Liu <shuntian.liu2@cloud.com> - 24.1.0-46
- Bump release and rebuild

* Fri Mar 07 2025 Vincent Liu <shuntian.liu2@cloud.com> - 24.1.0-45
- Bump release and rebuild

* Mon Mar 03 2025 Vincent Liu <shuntian.liu2@cloud.com> - 24.1.0-44
- Bump release and rebuild

* Wed Feb 26 2025 Vincent Liu <shuntian.liu2@cloud.com> - 24.1.0-43
- Bump release and rebuild

* Mon Feb 24 2025 Vincent Liu <shuntian.liu2@cloud.com> - 24.1.0-42
- Bump release and rebuild

* Wed Feb 12 2025 Vincent Liu <shuntian.liu2@cloud.com> - 24.1.0-41
- Bump release and rebuild

* Mon Feb 10 2025 Vincent Liu <shuntian.liu2@cloud.com> - 24.1.0-40
- Bump release and rebuild

* Mon Feb 03 2025 Vincent Liu <shuntian.liu2@cloud.com> - 24.1.0-39
- Bump release and rebuild

* Wed Jan 29 2025 Vincent Liu <shuntian.liu2@cloud.com> - 24.1.0-38
- Bump release and rebuild

* Mon Jan 27 2025 Vincent Liu <shuntian.liu2@cloud.com> - 24.1.0-37
- Bump release and rebuild

* Fri Jan 17 2025 Gang Ji <gang.ji@cloud.com> - 24.1.0-36
- Bump release and rebuild

* Mon Jan 13 2025 Gang Ji <gang.ji@cloud.com> - 24.1.0-35
- Bump release and rebuild

* Thu Jan 09 2025 Gang Ji <gang.ji@cloud.com> - 24.1.0-34
- Bump release and rebuild

* Wed Dec 18 2024 Gang Ji <gang.ji@cloud.com> - 24.1.0-33
- Bump release and rebuild

* Mon Nov 25 2024 Gang Ji <gang.ji@cloud.com> - 24.1.0-32
- Bump release and rebuild

* Wed Nov 13 2024 Christian Lindig <christian.lindig@cloud.com> - 24.1.0-31
- Bump release and rebuild

* Tue Nov 12 2024 Christian Lindig <christian.lindig@cloud.com> - 24.1.0-30
- Bump release and rebuild

* Mon Nov 11 2024 Christian Lindig <christian.lindig@cloud.com> - 24.1.0-29
- Bump release and rebuild

* Tue Oct 29 2024 Christian Lindig <christian.lindig@cloud.com> - 24.1.0-28
- Bump release and rebuild

* Wed Oct 23 2024 Christian Lindig <christian.lindig@cloud.com> - 24.1.0-27
- Bump release and rebuild

* Mon Oct 21 2024 Christian Lindig <christian.lindig@cloud.com> - 24.1.0-26
- Bump release and rebuild

* Mon Oct 14 2024 Christian Lindig <christian.lindig@cloud.com> - 24.1.0-25
- Bump release and rebuild

* Thu Oct 10 2024 Christian Lindig <christian.lindig@cloud.com> - 24.1.0-24
- Bump release and rebuild

* Thu Oct 03 2024 Christian Lindig <christian.lindig@citrix.com> - 24.1.0-23
- Bump release and rebuild

* Mon Sep 23 2024 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 24.1.0-22
- Bump release and rebuild

* Mon Sep 16 2024 Christian Lindig <christian.lindig@citrix.com> - 24.1.0-21
- Bump release and rebuild

* Tue Sep 10 2024 Christian Lindig <christian.lindig@citrix.com> - 24.1.0-20
- Bump release and rebuild

* Thu Sep 05 2024 Christian Lindig <christian.lindig@citrix.com> - 24.1.0-19
- Bump release and rebuild

* Wed Sep 04 2024 Christian Lindig <christian.lindig@citrix.com> - 24.1.0-18
- Bump release and rebuild

* Thu Aug 29 2024 Christian Lindig <christian.lindig@citrix.com> - 24.1.0-15
- Bump release and rebuild

* Thu Aug 22 2024 Christian Lindig <christian.lindig@citrix.com> - 24.1.0-14
- Bump release and rebuild

* Tue Aug 20 2024 Christian Lindig <christian.lindig@citrix.com> - 24.1.0-13
- Bump release and rebuild

* Thu Aug 15 2024 Ming Lu <ming.lu@cloud.com> - 24.1.0-12
- Bump release and rebuild

* Fri Jul 26 2024 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 24.1.0-11
- Bump release and rebuild

* Thu Jul 25 2024 Ming Lu <ming.lu@cloud.com> - 24.1.0-10
- Bump release and rebuild

* Wed Jul 24 2024 Ming Lu <ming.lu@cloud.com> - 24.1.0-9
- Bump release and rebuild

* Tue Jul 16 2024 Ming Lu <ming.lu@cloud.com> - 24.1.0-8
- Bump release and rebuild

* Tue Jul 09 2024 Ming Lu <ming.lu@cloud.com> - 24.1.0-7
- Bump release and rebuild

* Tue Jul 09 2024 Ming Lu <ming.lu@cloud.com> - 24.1.0-6
- Bump release and rebuild

* Mon Jul 01 2024 Ming Lu <ming.lu@cloud.com> - 24.1.0-5
- Bump release and rebuild

* Tue Jun 18 2024 Ming Lu <ming.lu@cloud.com> - 24.1.0-4
- Bump release and rebuild

* Mon Jun 10 2024 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 24.1.0-3
- Bump release and rebuild

* Thu Jun 06 2024 Ming Lu <ming.lu@cloud.com> - 24.1.0-2
- Bump release and rebuild

* Thu May 23 2024 Ming Lu <ming.lu@cloud.com> - 24.1.0-1
- CP-48969: log only first time that NVML can't be opened
- ci: update all actions

* Tue Apr 30 2024 Rob Hoes <rob.hoes@citrix.com> - 24.0.0-4
- Bump release and rebuild

* Mon Apr 15 2024 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 24.0.0-3
- Bump release and rebuild

* Tue Apr 09 2024 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 24.0.0-2
- Bump release and rebuild

* Mon Mar 18 2024 Rob Hoes <rob.hoes@citrix.com> - 24.0.0-1
- Re-release with new version number consistent with xapi's version scheme

* Mon Mar 18 2024 Rob Hoes <rob.hoes@citrix.com> - 0.25.0-15
- Bump release and rebuild

* Thu Feb 29 2024 Rob Hoes <rob.hoes@citrix.com> - 0.25.0-14
- Bump release and rebuild

* Thu Feb 15 2024 Rob Hoes <rob.hoes@citrix.com> - 0.25.0-13
- Bump release and rebuild

* Mon Feb 12 2024 Rob Hoes <rob.hoes@citrix.com> - 0.25.0-12
- Bump release and rebuild

* Tue Jan 30 2024 Rob Hoes <rob.hoes@citrix.com> - 0.25.0-11
- Bump release and rebuild

* Thu Jan 25 2024 Rob Hoes <rob.hoes@citrix.com> - 0.25.0-10
- Bump release and rebuild

* Tue Jan 16 2024 Rob Hoes <rob.hoes@citrix.com> - 0.25.0-9
- Bump release and rebuild

* Wed Jan 10 2024 Rob Hoes <rob.hoes@citrix.com> - 0.25.0-8
- Bump release and rebuild

* Tue Dec 19 2023 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 0.25.0-7
- Bump release and rebuild

* Mon Dec 04 2023 Rob Hoes <rob.hoes@citrix.com> - 0.25.0-6
- Bump release and rebuild

* Fri Nov 10 2023 Rob Hoes <rob.hoes@citrix.com> - 0.25.0-5
- Bump release and rebuild

* Mon Oct 30 2023 Rob Hoes <rob.hoes@citrix.com> - 0.25.0-4
- Bump release and rebuild

* Mon Oct 16 2023 Rob Hoes <rob.hoes@citrix.com> - 0.25.0-3
- Bump release and rebuild

* Wed Oct 11 2023 Rob Hoes <rob.hoes@citrix.com> - 0.25.0-2
- Bump release and rebuild

* Thu Aug 31 2023 Rob Hoes <rob.hoes@citrix.com> - 0.25.0-1
- Log PID on exit; make message more explicit

* Fri Aug 18 2023 Rob Hoes <rob.hoes@citrix.com> - 0.24.0-29
- Bump release and rebuild

* Tue Aug 15 2023 Rob Hoes <rob.hoes@citrix.com> - 0.24.0-28
- Bump release and rebuild

* Thu Aug 03 2023 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 0.24.0-27
- Bump release and rebuild

* Wed Aug 02 2023 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 0.24.0-26
- Bump release and rebuild

* Thu Jul 27 2023 Rob Hoes <rob.hoes@citrix.com> - 0.24.0-25
- Bump release and rebuild

* Thu Jul 20 2023 Rob Hoes <rob.hoes@citrix.com> - 0.24.0-24
- Bump release and rebuild

* Mon Jul 17 2023 Edwin Török <edwin.torok@cloud.com> - 0.24.0-23
- Bump release and rebuild

* Tue Jul 11 2023 Rob Hoes <rob.hoes@citrix.com> - 0.24.0-22
- Bump release and rebuild

* Mon Jun 19 2023 Rob Hoes <rob.hoes@citrix.com> - 0.24.0-21
- Bump release and rebuild

* Fri Jun 09 2023 Rob Hoes <rob.hoes@citrix.com> - 0.24.0-20
- Bump release and rebuild

* Wed Jun 07 2023 Rob Hoes <rob.hoes@citrix.com> - 0.24.0-19
- Bump release and rebuild

* Tue Jun 06 2023 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 0.24.0-18
- Bump release and rebuild

* Thu May 25 2023 Rob Hoes <rob.hoes@citrix.com> - 0.24.0-17
- Bump release and rebuild

* Tue May 09 2023 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 0.24.0-16
- Bump release and rebuild

* Wed Apr 19 2023 Rob Hoes <rob.hoes@citrix.com> - 0.24.0-15
- Bump release and rebuild

* Fri Apr 14 2023 Christian Lindig <christian.lindig@citrix.com> - 0.24.0-14
- XSI-1404 increase StartLimitBurst to 25

* Fri Mar 24 2023 Rob Hoes <rob.hoes@citrix.com> - 0.24.0-13
- Bump release and rebuild

* Wed Mar 08 2023 Rob Hoes <rob.hoes@citrix.com> - 0.24.0-12
- Bump release and rebuild

* Thu Mar 02 2023 Rob Hoes <rob.hoes@citrix.com> - 0.24.0-11
- Bump release and rebuild

* Mon Feb 20 2023 Rob Hoes <rob.hoes@citrix.com> - 0.24.0-10
- Bump release and rebuild

* Fri Feb 10 2023 Rob Hoes <rob.hoes@citrix.com> - 0.24.0-9
- Bump release and rebuild

* Wed Feb 08 2023 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 0.24.0-8
- Bump release and rebuild

* Thu Feb 02 2023 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 0.24.0-7
- Bump release and rebuild

* Mon Jan 30 2023 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 0.24.0-6
- Bump release and rebuild

* Mon Jan 30 2023 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 0.24.0-5
- Bump release and rebuild

* Fri Jan 27 2023 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 0.24.0-4
- Bump release and rebuild

* Thu Jan 26 2023 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 0.24.0-3
- Bump release and rebuild

* Mon Jan 23 2023 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 0.24.0-2
- Bump release and rebuild

* Thu Jan 19 2023 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 0.24.0-1
- CP-33044 Introduce NVML.{attach,detach}

* Mon Dec 12 2022 Rob Hoes <rob.hoes@citrix.com> - 0.23.0-2
- Bump release and rebuild

* Thu Dec 08 2022 Rob Hoes <rob.hoes@citrix.com> - 0.23.0-1
- CP-33044 add Make target "unmock"
- CP-33044 Provide mock impl for NVML attach/detach
- gpumon: add a unit test to check that gpumon doesn't fail on startup due to unbound API calls

* Fri Nov 18 2022 Rob Hoes <rob.hoes@citrix.com> - 0.22.0-1
- CA-371894 fix bindings that use dynamic allocation for results
- CA-371894 fix some const warnings

* Tue Nov 01 2022 Rob Hoes <rob.hoes@citrix.com> - 0.21.0-1
- CP-37861 - don't include nvml_grid.h

* Wed Oct 12 2022 Rob Hoes <rob.hoes@citrix.com> - 0.20.0-28
- Bump release and rebuild

* Tue Oct 04 2022 Rob Hoes <rob.hoes@citrix.com> - 0.20.0-27
- Bump release and rebuild

* Fri Sep 09 2022 Rob Hoes <rob.hoes@citrix.com> - 0.20.0-26
- Bump release and rebuild

* Mon Aug 22 2022 Rob Hoes <rob.hoes@citrix.com> - 0.20.0-25
- Bump release and rebuild

* Mon Aug 08 2022 Pau Ruiz Safont <pau.safont@citrix.com> - 0.20.0-24
- Bump release and rebuild

* Fri Jul 29 2022 Rob Hoes <rob.hoes@citrix.com> - 0.20.0-23
- Bump release and rebuild

* Wed Jul 06 2022 Rob Hoes <rob.hoes@citrix.com> - 0.20.0-22
- Bump release and rebuild

* Tue Jul 05 2022 Pau Ruiz Safont <pau.safont@citrix.com> - 0.20.0-21
- Bump release and rebuild

* Mon Jun 27 2022 Rob Hoes <rob.hoes@citrix.com> - 0.20.0-20
- Bump release and rebuild

* Wed Jun 08 2022 Rob Hoes <rob.hoes@citrix.com> - 0.20.0-19
- Bump release and rebuild

* Wed May 18 2022 Rob Hoes <rob.hoes@citrix.com> - 0.20.0-18
- Bump release and rebuild

* Wed Apr 27 2022 Rob Hoes <rob.hoes@citrix.com> - 0.20.0-17
- Bump release and rebuild

* Tue Apr 19 2022 Rob Hoes <rob.hoes@citrix.com> - 0.20.0-16
- Bump release and rebuild

* Wed Apr 13 2022 Rob Hoes <rob.hoes@citrix.com> - 0.20.0-15
- Bump release and rebuild

* Fri Apr 01 2022 Rob Hoes <rob.hoes@citrix.com> - 0.20.0-14
- Bump release and rebuild

* Mon Mar 28 2022 Rob Hoes <rob.hoes@citrix.com> - 0.20.0-13
- Bump release and rebuild

* Tue Mar 15 2022 Rob Hoes <rob.hoes@citrix.com> - 0.20.0-12
- Bump release and rebuild

* Thu Mar 03 2022 Rob Hoes <rob.hoes@citrix.com> - 0.20.0-11
- Bump release and rebuild

* Mon Feb 28 2022 Rob Hoes <rob.hoes@citrix.com> - 0.20.0-10
- Bump release and rebuild

* Mon Feb 21 2022 Rob Hoes <rob.hoes@citrix.com> - 0.20.0-9
- Bump release and rebuild

* Tue Feb 15 2022 Rob Hoes <rob.hoes@citrix.com> - 0.20.0-8
- Bump release and rebuild with OCaml 4.13.1 compiler.

* Mon Feb 14 2022 Rob Hoes <rob.hoes@citrix.com> - 0.20.0-7
- Bump release and rebuild

* Wed Feb 09 2022 Rob Hoes <rob.hoes@citrix.com> - 0.20.0-6
- Bump release and rebuild

* Thu Feb 03 2022 Rob Hoes <rob.hoes@citrix.com> - 0.20.0-5
- Bump release and rebuild

* Wed Jan 26 2022 Rob Hoes <rob.hoes@citrix.com> - 0.20.0-4
- Bump release and rebuild

* Tue Jan 11 2022 Rob Hoes <rob.hoes@citrix.com> - 0.20.0-3
- Bump release and rebuild

* Fri Dec 17 2021 Rob Hoes <rob.hoes@citrix.com> - 0.20.0-2
- Bump release and rebuild

* Fri Dec 03 2021 Rob Hoes <rob.hoes@citrix.com> - 0.20.0-1
- maintenance: run ocamlformat
- CP-33121: Drop stdext_std usage
- maintenance: use github actions for CI
- maintenance: stop using travis for CI

* Thu Nov 25 2021 Rob Hoes <rob.hoes@citrix.com> - 0.19.0-42
- Bump release and rebuild

* Thu Nov 25 2021 Rob Hoes <rob.hoes@citrix.com> - 0.19.0-41
- Bump release and rebuild

* Wed Nov 24 2021 Edwin Török <edvin.torok@citrix.com> - 0.19.0-40
- Bump release and rebuild

* Wed Nov 24 2021 Edwin Török <edvin.torok@citrix.com> - 0.19.0-39
- Bump release and rebuild

* Fri Nov 19 2021 Rob Hoes <rob.hoes@citrix.com> - 0.19.0-38
- Bump release and rebuild

* Mon Nov 08 2021 Christian Lindig <christian.lindig@citrix.com> - 0.19.0-37
- Bump release and rebuild

* Mon Oct 11 2021 Rob Hoes <rob.hoes@citrix.com> - 0.19.0-36
- Bump release and rebuild

* Fri Oct 01 2021 Rob Hoes <rob.hoes@citrix.com> - 0.19.0-35
- Bump release and rebuild

* Wed Sep 22 2021 Rob Hoes <rob.hoes@citrix.com> - 0.19.0-34
- Bump release and rebuild

* Thu Sep 16 2021 Rob Hoes <rob.hoes@citrix.com> - 0.19.0-33
- Bump release and rebuild

* Fri Sep 03 2021 Rob Hoes <rob.hoes@citrix.com> - 0.19.0-32
- Bump release and rebuild

* Wed Sep 01 2021 Rob Hoes <rob.hoes@citrix.com> - 0.19.0-31
- Bump release and rebuild

* Thu Aug 26 2021 Christian Lindig <christian.lindig@citrix.com> - 0.19.0-30
- Bump release and rebuild

* Wed Aug 25 2021 Christian Lindig <christian.lindig@citrix.com> - 0.19.0-29
- Bump release and rebuild

* Wed Aug 25 2021 Christian Lindig <christian.lindig@citrix.com> - 0.19.0-28
- Bump release and rebuild

* Thu Jul 29 2021 Rob Hoes <rob.hoes@citrix.com> - 0.19.0-27
- Bump release and rebuild

* Mon Jul 19 2021 Rob Hoes <rob.hoes@citrix.com> - 0.19.0-26
- Bump release and rebuild

* Thu Jul 08 2021 Christian Lindig <christian.lindig@citrix.com> - 0.19.0-25
- Bump release and rebuild

* Thu May 20 2021 Rob Hoes <rob.hoes@citrix.com> - 0.19.0-21
- Bump release and rebuild

* Mon May 17 2021 Rob Hoes <rob.hoes@citrix.com> - 0.19.0-20
- Bump release and rebuild

* Mon May 10 2021 Rob Hoes <rob.hoes@citrix.com> - 0.19.0-19
- Bump release and rebuild

* Fri May 07 2021 Rob Hoes <rob.hoes@citrix.com> - 0.19.0-18
- Bump release and rebuild

* Thu May 06 2021 Rob Hoes <rob.hoes@citrix.com> - 0.19.0-17
- Bump release and rebuild

* Tue Apr 27 2021 Rob Hoes <rob.hoes@citrix.com> - 0.19.0-16
- Bump release and rebuild

* Thu Apr 22 2021 Rob Hoes <rob.hoes@citrix.com> - 0.19.0-15
- Bump release and rebuild

* Wed Apr 14 2021 Rob Hoes <rob.hoes@citrix.com> - 0.19.0-14
- Bump release and rebuild

* Wed Apr 14 2021 Rob Hoes <rob.hoes@citrix.com> - 0.19.0-13
- Bump release and rebuild

* Thu Apr 01 2021 Rob Hoes <rob.hoes@citrix.com> - 0.19.0-12
- Bump release and rebuild

* Fri Mar 26 2021 Rob Hoes <rob.hoes@citrix.com> - 0.19.0-11
- Bump release and rebuild

* Mon Mar 22 2021 Andrew Cooper <andrew.cooper3@citrix.com> - 0.19.0-10
- Drop incorrect BuildRequires

* Mon Mar 08 2021 Rob Hoes <rob.hoes@citrix.com> - 0.19.0-9
- Bump release and rebuild

* Fri Mar 05 2021 Rob Hoes <rob.hoes@citrix.com> - 0.19.0-8
- Bump release and rebuild

* Tue Mar 02 2021 Rob Hoes <rob.hoes@citrix.com> - 0.19.0-7
- Bump release and rebuild

* Tue Feb 23 2021 Rob Hoes <rob.hoes@citrix.com> - 0.19.0-6
- Bump release and rebuild

* Tue Feb 16 2021 Rob Hoes <rob.hoes@citrix.com> - 0.19.0-5
- Bump release and rebuild

* Fri Feb 05 2021 Rob Hoes <rob.hoes@citrix.com> - 0.19.0-4
- Bump release and rebuild

* Thu Jan 28 2021 Rob Hoes <rob.hoes@citrix.com> - 0.19.0-3
- Bump release and rebuild

* Wed Jan 06 2021 Rob Hoes <rob.hoes@citrix.com> - 0.19.0-2
- Bump release and rebuild

* Tue Sep 22 2020 Christian Lindig <christian.lindig@citrix.com> - 0.19.0-1
- maintenance: move to Dune 2.0, ocamlformat

* Fri Apr 17 2020 Christian Lindig <christian.lindig@citrix.com> - 0.18.0-1
- CP-28222: pick environment valriables from xs-opam for CI
- CP-33121: Remove direct use of stdext

* Fri Aug 23 2019 Edwin Török <edvin.torok@citrix.com> - 0.17.0-2
- bump packages after xs-opam update

* Wed Jun 05 2019 Christian Lindig <christian.lindig@citrix.com> - 0.17.0-1
- CP-31124: Receive uuid from Xapi and use it to filter metadata.
- Add mock for get_vgpu_for_uuid.

* Thu Mar 14 2019 Christian Lindig <christian.lindig@citrix.com> - 0.16.0-1
- Use Dune profile release
- Add logging around signal handling
- Check return value of malloc()
- Use OCaml 4.07 for Travis

* Tue Dec 04 2018 Christian Lindig <christian.lindig@citrix.com> - 0.15.0-1
- Deprecated xcp in favour of xapi-idl.

* Fri Nov 16 2018 Christian Lindig <christian.lindig@citrix.com> - 0.14.0-1
- New ocaml-rpc

* Thu Oct 25 2018 Christian Lindig <christian.lindig@citrix.com> - 0.13.0-1
- XSI-131 use correct versioned interface fn's

* Tue Oct 09 2018 Christian Lindig <christian.lindig@citrix.com> - 0.12.0-1
- CP-29621 Port from Oasis to Dune
- CP-29621 Make Travis work using mock modules

* Mon Feb 19 2018 Christian Lindig <christian.lindig@citrix.com> - 0.11.0-1
- Use String.lowercase_ascii over deprecated String.lowercase
- CA-283715: Bind API call declarations to implementations
- CA-283715: gpumon, gpumon_server: rationalise module interfaces

* Thu Feb 08 2018 Christian Lindig <christian.lindig@citrix.com> - 0.10.0-1
- CP-26717: Port Gpumon daemon to PPX-based RPCs

* Wed Jan 17 2018 Christian Lindig <christian.lindig@citrix.com> - 0.9.0-1
- CA-280209 NVidia vGPU migration driver: use >= 390

* Tue Jan 16 2018 Christian Lindig <christian.lindig@citrix.com> - 0.8.0-1
- CA-275983 make providing pGPU metadata version dependent

* Fri Dec 15 2017 Christian Lindig <christian.lindig@citrix.com> - 0.7.0-1
- CP-24185 add get_pgpu_vgpu_compatibility()
- CP-24185 refactor get_pgpu_vgpu_compatibility
- CP-24185 add Gpumon_server.get_vgpu_metadata()
- CP-24185 add C binding get_vgpu_metadata()

* Wed Nov 01 2017 Rob Hoes <rob.hoes@citrix.com> - 0.6.0-1
- CP-19615: Introduce nvml_grid bindings and additional relevant bindings
- CP-20676: Add stubs for vGPU compatibility checks
- CP-20677: implement gpumon server interface and manage idl server

* Thu Apr 27 2017 Rob Hoes <rob.hoes@citrix.com> - 0.5.0-1
- Change license to ISC

* Mon Mar 13 2017 Marcello Seri <marcello.seri@citrix.com> - 0.4.0-2
- Update OCaml dependencies and build/install script after xs-opam-repo split

* Thu Mar 02 2017 Gabor Igloi <gabor.igloi@citrix.com> - 0.4.0-1
- Port to xs-opam-repo providing updated OCaml libraries;
  fix compilation issues under ocaml 4.02.3: rename conflicting Config module,
  replace custom Result with Rresult

* Fri Feb 17 2017 Frederico Mazzone <frederico.mazzone@citrix.com> - 0.3.2-2
- CA-243676: Do not restart toolstack services on RPM upgrade

* Thu Dec 15 2016 Rob Hoes <rob.hoes@citrix.com> - 0.3.2-1
- git: Add metadata to the result of `git archive`

* Mon Nov 21 2016 Rob Hoes <rob.hoes@citrix.com> - 0.3.1-2
- Install systemd service files with 644 permissions (non-executable)

* Wed Oct 19 2016 Euan Harris <euan.harris@citrix.com> - 0.3.1-1
- Remove final vestiges of previous init system

* Mon Aug 22 2016 Rafal Mielniczuk <rafal.mielniczuk@citrix.com> - 0.3.0-2
- Package for systemd

* Tue Aug 16 2016 Christian Lindig <christian.lindig@citrix.com> - 0.3.0-1
- Update to 0.3.0 for new upstream release

* Mon May 16 2016 Si Beaumont <simon.beaumont@citrix.com> - 0.2.0-2
- Re-run chkconfig on upgrade
- Stop service on uninstall

* Tue Apr 26 2016 Si Beaumont <simon.beaumont@citrix.com> - 0.2.0-1
- Update to 0.2.0

* Mon Nov 10 2014 John Else <john.else@citrix.com> - 0.1.0-1
- Initial package for planex
