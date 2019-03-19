Name:           gpumon
Version:        0.11.0
Release:        5%{?dist}
Summary:        RRDD GPU metrics plugin
Group:          System/Hypervisor
License:        ISC
URL:            https://github.com/xenserver/gpumon
Source0:        https://code.citrite.net/rest/archive/latest/projects/XSU/repos/%{name}/archive?at=v%{version}&format=tar.gz&prefix=%{name}-%{version}#/%{name}-%{version}.tar.gz
Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/gpumon/archive?at=v0.11.0&format=tar.gz&prefix=gpumon-0.11.0#/gpumon-0.11.0.tar.gz) = 291422b669f42940f5c259b558a773fff2b9ddd8
Source1:        xcp-rrdd-gpumon.service
BuildRoot:      %{_tmppath}/%{name}-%{version}-root
BuildRequires:  gdk-devel
BuildRequires:  xs-opam-repo
BuildRequires:  ocaml-rrdd-plugin-devel
%{?systemd_requires}
BuildRequires:  systemd
BuildRequires:  xen-dom0-libs-devel

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
