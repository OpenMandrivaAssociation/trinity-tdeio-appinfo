%bcond clang 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

%define tde_pkg tdeio-appinfo
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	0.3
Release:	%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:	TDEIO slave for the appinfo protocol
Group:		Productivity/Networking/Ftp/Clients
URL:		http://lukeplant.me.uk/kio-appinfo/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/tdeio/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DWITH_ALL_OPTIONS=ON
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DBUILD_DOC=ON
BuildOption:    -DBUILD_TRANSLATIONS=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	fdupes

# ACL support
BuildRequires:  pkgconfig(libacl)

# IDN support
BuildRequires:	pkgconfig(libidn)

# OPENSSL support
BuildRequires:  pkgconfig(openssl)


BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)


%description
Adds support for the "appinfo:" protocol
to Konqueror and other TDE applications.
.
This enables you to perform appinfo: searches in TDE.


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README.md
%{tde_prefix}/%{_lib}/trinity/tdeio_appinfo.la
%{tde_prefix}/%{_lib}/trinity/tdeio_appinfo.so
%{tde_prefix}/share/services/appinfo.protocol
%lang(it) %{tde_prefix}/share/locale/it/LC_MESSAGES/tdeio_appinfo.mo
%lang(ka) %{tde_prefix}/share/locale/ka/LC_MESSAGES/tdeio_appinfo.mo
%lang(nl) %{tde_prefix}/share/locale/nl/LC_MESSAGES/tdeio_appinfo.mo
%lang(pl) %{tde_prefix}/share/locale/pl/LC_MESSAGES/tdeio_appinfo.mo
%lang(ru) %{tde_prefix}/share/locale/ru/LC_MESSAGES/tdeio_appinfo.mo

