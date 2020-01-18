
%global qt_module qtquickcontrols

%define docs 1

Name:    qt5-%{qt_module}
Summary: Qt5 - module with set of QtQuick controls
Version: 5.6.2
Release: 1%{?dist}

License: LGPLv2 or LGPLv3 and GFDL
Url:     http://www.qt.io
Source0: http://download.qt.io/official_releases/qt/5.6/%{version}/submodules/%{qt_module}-opensource-src-%{version}.tar.xz

BuildRequires:  qt5-qtbase-devel >= %{version}
BuildRequires:  qt5-qtbase-static >= %{version}

BuildRequires:  qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
BuildRequires:  qt5-qtdeclarative-private-devel
%{?_qt5:Requires: qt5-qtdeclarative%{?_isa} = %{_qt5_version}}

%description
The Qt Quick Controls module provides a set of controls that can be used to
build complete interfaces in Qt Quick.

%if 0%{?docs}
%package doc
Summary: API documentation for %{name}
License: GFDL
Requires: %{name} = %{version}-%{release}
BuildRequires: qt5-qdoc
BuildRequires: qt5-qhelpgenerator
BuildArch: noarch
%description doc
%{summary}.
%endif

%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.


%prep
%setup -q -n %{qt_module}-opensource-src-%{version}


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{qmake_qt5} ..

make %{?_smp_mflags}

%if 0%{?docs}
# HACK to avoid multilib conflicts in noarch content
# see also https://bugreports.qt-project.org/browse/QTBUG-42071
QT_HASH_SEED=0; export QT_HASH_SEED
make %{?_smp_mflags} docs
%endif
popd


%install
make install INSTALL_ROOT=%{buildroot} -C %{_target_platform}

%if 0%{?docs}
make install_docs INSTALL_ROOT=%{buildroot} -C %{_target_platform}
%endif


%files
%{_qt5_archdatadir}/qml/QtQuick/
%doc LICENSE.*

%if 0%{?docs}
%files doc
%doc LICENSE.FDL
%{_qt5_docdir}/qtquickcontrols.qch
%{_qt5_docdir}/qtquickcontrols/
%{_qt5_docdir}/qtquicklayouts.qch
%{_qt5_docdir}/qtquicklayouts/
%{_qt5_docdir}/qtquickdialogs.qch
%{_qt5_docdir}/qtquickdialogs/
%{_qt5_docdir}/qtquickextras.qch
%{_qt5_docdir}/qtquickextras/
%endif

%if 0%{?_qt5_examplesdir:1}
%files examples
%{_qt5_examplesdir}/
%endif


%changelog
* Wed Jan 11 2017 Jan Grulich <jgrulich@redhat.com> - 5.6.2-1
- Update to 5.6.2
  Resolves: bz#1384824

* Tue Aug 30 2016 Jan Grulich <jgrulich@redhat.com> - 5.6.1-10
- Increase build version to have newer version than in EPEL
  Resolves: bz#1317408

* Wed Jun 08 2016 Jan Grulich <jgrulich@redhat.com> - 5.6.1-1
- Update to 5.6.1
  Resolves: bz#1317408

* Wed Apr 13 2016 Jan Grulich <jgrulich@redhat.com> - 5.6.0-5
- Enable documentation
  Resolves: bz#1317408

* Thu Apr 07 2016 Jan Grulich <jgrulich@redhat.com> - 5.6.0-4
- Initial version for RHEL
  Resolves: bz#1317408

* Sun Mar 20 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.0-3
- rebuild

* Fri Mar 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.0-2
- rebuild

* Mon Mar 14 2016 Helio Chissini de Castro <helio@kde.org> - 5.6.0-1
- 5.6.0 final release

* Tue Feb 23 2016 Helio Chissini de Castro <helio@kde.org> - 5.6.0-0.8.rc
- Update to final RC

* Sun Feb 21 2016 Rex Dieter <rdieter@fedoraproject.org> 5.6.0-0.7.rc
- rebuild

* Mon Feb 15 2016 Helio Chissini de Castro <helio@kde.org> - 5.6.0-0.6
- Update RC release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0-0.5.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 21 2015 Rex Dieter <rdieter@fedoraproject.org> 5.6.0-0.4
- fix source URL, fresh (real?) beta sources, fix Release:, move qdoc dep to -doc

* Thu Dec 10 2015 Helio Chissini de Castro <helio@kde.org> - 5.6.0-0.3
- Official beta release

* Tue Nov 03 2015 Helio Chissini de Castro <helio@kde.org> - 5.6.0-0.1
- Start to implement 5.6.0 beta

* Thu Oct 15 2015 Helio Chissini de Castro <helio@kde.org> - 5.5.1-2
- Update to final release 5.5.1

* Tue Sep 29 2015 Helio Chissini de Castro <helio@kde.org> - 5.5.1-1
- Update to Qt 5.5.1 RC1

* Wed Jul 29 2015 Rex Dieter <rdieter@fedoraproject.org> 5.5.0-3
- -docs: BuildRequires: qt5-qhelpgenerator, standardize bootstrapping

* Thu Jul 16 2015 Rex Dieter <rdieter@fedoraproject.org> 5.5.0-2
- tighten deps (#1233829), .spec cosmetics

* Wed Jul 1 2015 Helio Chissini de Castro <helio@kde.org> 5.5.0-1
- New final upstream release Qt 5.5.0

* Thu Jun 25 2015 Helio Chissini de Castro <helio@kde.org> - 5.5.0-0.2.rc
- Update for official RC1 released packages

* Wed Jun 17 2015 Daniel Vrátil <dvratil@redhat.com> - 5.5.0-0.1.rc
- Qt 5.5.0 RC1

* Wed Jun 03 2015 Jan Grulich <jgrulich@redhat.com> -5.4.2-1
- 5.4.2

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 5.4.1-3
- Rebuilt for GCC 5 C++11 ABI change

* Fri Feb 27 2015 Rex Dieter <rdieter@fedoraproject.org> - 5.4.1-2
- rebuild (gcc5)

* Tue Feb 24 2015 Jan Grulich <jgrulich@redhat.com> 5.4.1-1
- 5.4.1

* Wed Dec 10 2014 Rex Dieter <rdieter@fedoraproject.org> 5.4.0-1
- 5.4.0 (final)

* Fri Nov 28 2014 Rex Dieter <rdieter@fedoraproject.org> 5.4.0-0.3.rc
- 5.4.0-rc

* Mon Nov 03 2014 Rex Dieter <rdieter@fedoraproject.org> 5.4.0-0.2.beta
- out-of-tree build, use %%qmake_qt5

* Sun Oct 19 2014 Rex Dieter <rdieter@fedoraproject.org> 5.4.0-0.1.beta
- 5.4.0-beta

* Wed Sep 17 2014 Rex Dieter <rdieter@fedoraproject.org> - 5.3.2-1
- 5.3.2

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 17 2014 Jan Grulich <jgrulich@redhat.com> - 5.3.1-1
- 5.3.1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Jan Grulich <jgrulich@redhat.com> 5.3.0-1
- 5.3.0

* Thu Feb 06 2014 Rex Dieter <rdieter@fedoraproject.org> 5.2.1-1
- 5.2.1

* Mon Jan 27 2014 Rex Dieter <rdieter@fedoraproject.org> 5.2.0-2
- ready -examples subpkg

* Thu Dec 12 2013 Rex Dieter <rdieter@fedoraproject.org> 5.2.0-1
- 5.2.0

* Mon Dec 02 2013 Rex Dieter <rdieter@fedoraproject.org> 5.2.0-0.10.rc1
- 5.2.0-rc1

* Mon Nov 11 2013 Rex Dieter <rdieter@fedoraproject.org> 5.2.0-0.5.beta1
- rebuild (arm/qreal)

* Thu Oct 24 2013 Rex Dieter <rdieter@fedoraproject.org> 5.2.0-0.4.beta1
- 5.2.0-beta1

* Thu Oct 24 2013 Rex Dieter <rdieter@fedoraproject.org> 5.2.0-0.3.alpha
- bootstrap ppc

* Thu Oct 24 2013 Lubomir Rintel <lkundrak@v3.sk> - 5.2.0-0.2.alpha
- Bulk sad and useless attempt at consistent SPEC file formatting

* Wed Oct 02 2013 Rex Dieter <rdieter@fedoraproject.org> - 5.2.0-0.1.alpha
- 5.2.0-alpha
- tidy dir ownership
- -doc subpkg

* Mon Sep 23 2013 Lubomir Rintel <lkundrak@v3.sk> - 5.1.1-2
- Drop unused devel package (Rex Dieter, #1008527)

* Wed Sep 11 2013 Lubomir Rintel <lkundrak@v3.sk> - 5.1.1-1
- Initial packaging
