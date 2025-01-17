%global package_speccommit d0964d335e8e3e02b8f777120f5c46e0339f720e
%global package_srccommit v0.18.0
Name:           gpumon
Version: 0.18.0
Release: 23.1%{?xsrel}%{?dist}
Summary:        RRDD GPU metrics plugin
Group:          System/Hypervisor
License:        ISC
URL:            https://github.com/xenserver/gpumon
Source0: gpumon-0.18.0.tar.gz
Source1: xcp-rrdd-gpumon.service
BuildRoot:      %{_tmppath}/%{name}-%{version}-root
# XCP-ng: Removed because it includes proprietary components
# BuildRequires:  gdk-devel
BuildRequires:  xs-opam-repo
BuildRequires:  ocaml-rrdd-plugin-devel
%{?systemd_requires}
BuildRequires:  systemd
BuildRequires:  xen-ocaml-devel

Requires:       libev

%description
This package contains a plugin registering to the RRD daemon and exposing GPU
metrics.

%prep
%autosetup -p1

%build
# XCP-ng: Add a `make mock` to avoid real build requiring proprietary element
DESTDIR=%{buildroot} %{__make} mock
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
* Thu Jan 16 2025 Gael Duperrey <gduperrey@vates.tech> - 0.18.0-23.1
- Rebuild after sync with hotfix XS82ECU1080
- No source changes: only rebuild for dependencies
- *** Upstream changelog ***
- * Fri Dec 13 2024 Christian Lindig <christian.lindig@cloud.com> - 0.18.0-23
- - Bump release and rebuild
- * Thu Dec 12 2024 Christian Lindig <christian.lindig@cloud.com> - 0.18.0-22
- - Bump release and rebuild
- * Mon Dec 09 2024 Christian Lindig <christian.lindig@cloud.com> - 0.18.0-21
- - Bump release and rebuild

* Thu Oct 24 2024 Gael Duperrey <gduperrey@vates.tech> - 0.18.0-20.1
- Rebuild after sync with hotfix XS82ECU1074
- No source changes: only rebuild for dependencies
- *** Upstream changelog ***
- * Thu Aug 29 2024 Christian Lindig <christian.lindig@cloud.com> - 0.18.0-20
- - Bump release and rebuild
- * Wed Jun 19 2024 Christian Lindig <christian.lindig@cloud.com> - 0.18.0-19
- - Bump release and rebuild

* Tue Jun 04 2024 Gael Duperrey <gduperrey@vates.tech> - 0.18.0-18.1
- Rebuild after sync with hotfix XS82ECU1064
- No source changes: only rebuild for dependencies
- *** Upstream changelog ***
- * Fri Mar 08 2024 Christian Lindig <christian.lindig@cloud.com> - 0.18.0-18
- - Bump release and rebuild
- * Wed Mar 06 2024 Christian Lindig <christian.lindig@cloud.com> - 0.18.0-17
- - Bump release and rebuild
- * Tue Mar 05 2024 Christian Lindig <christian.lindig@cloud.com> - 0.18.0-16
- - Bump release and rebuild
- * Fri Nov 03 2023 Christian Lindig <christian.lindig@cloud.com> - 0.18.0-15
- - Bump release and rebuild
- * Tue Oct 24 2023 Christian Lindig <christian.lindig@cloud.com> - 0.18.0-14
- - Bump release and rebuild
- * Tue Oct 24 2023 Christian Lindig <christian.lindig@cloud.com> - 0.18.0-13
- - Bump release and rebuild
- * Wed Oct 18 2023 Christian Lindig <christian.lindig@cloud.com> - 0.18.0-12
- - Bump release and rebuild

* Fri Nov 03 2023 Guillaume Thouvenin <guillaume.thouvenin@vates.tech> - 0.18.0-11.2
- Don't output to stdout/stderr (and thus daemon.log): there already are RRDD logs

* Fri Oct 13 2023 Samuel Verschelde <stormi-xcp@ylix.fr> - 0.18.0-11.1
- Rebuild after sync with hotfix XS82ECU1049
- No source changes: only rebuild for dependencies
- *** Upstream changelog ***
- * Mon Oct 02 2023 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 0.18.0-11
- - Bump release and rebuild

* Wed Aug 09 2023 Gael Duperrey <gduperrey@vates.fr> - 0.18.0-10.1
- Sync with hotfix XS82ECU1040
- *** Upstream changelog ***
- * Mon Jun 19 2023 Christian Lindig <christian.lindig@citrix.com> - 0.18.0-9
- - Bump release and rebuild
- * Thu Jun 08 2023 Christian Lindig <christian.lindig@citrix.com> - 0.18.0-8
- - Bump release and rebuild
- * Fri May 12 2023 Christian Lindig <christian.lindig@citrix.com> - 0.18.0-7
- - Bump release and rebuild
- * Wed Apr 19 2023 Christian Lindig <christian.lindig@citrix.com> - 0.18.0-6
- - XSI 1404 increase StartLimitBurst to 25, accept only 0 RC for scucess
- * Tue Feb 28 2023 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 0.18.0-5
- - Fix xen BuildReqs

* Thu Apr 27 2023 Samuel Verschelde <stormi-xcp@ylix.fr> - 0.18.0-4.3
- Rebuild for ocaml-rrdd-plugin-1.9.1-2.2.xcpng8.2
- Fixes "not enough memory" messages in xcp-rrdd-plugins.log

* Wed Aug 17 2022 Gael Duperrey <gduperrey@vates.fr> - 0.18.0-4.2
- Rebuild for updated xapi from XS82ECU1011

* Mon Jan 10 2022 Samuel Verschelde <stormi-xcp@ylix.fr> - 0.18.0-4.1
- Sync with CH 8.2.1
- *** Upstream changelog ***
- * Mon Sep 27 2021 Pau Ruiz Safont <pau.safont@citrix.com> - 0.18.0-4
- - Bump package for libev dependency
- * Mon Sep 27 2021 Pau Ruiz Safont <pau.safont@citrix.com> - 0.18.0-3
- - Bump package after xs-opam update
- * Tue Jul 13 2021 Edwin Török <edvin.torok@citrix.com> - 0.18.0-2
- - bump packages after xs-opam update

* Wed Jul 15 2020 Benjamin Reis <benjamin.reis@vates.fr> - 0.18.0-1.1
- Mock gpumon to build without proprietary element
- Related to xcp-ng/xcp#381

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
