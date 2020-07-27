Name:           check-sieve
Version:        0.6
Release:        2%{?dist}
Summary:        Syntax checker for mail sieves.

License:        MIT
URL:            https://github.com/dburkart/check-sieve
Source0:        https://github.com/dburkart/check-sieve/archive/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: bison >= 3.0.4
BuildRequires: flex >= 2.5.35
BuildRequires: python3-devel

%description
Syntax checker for mail sieves.

%prep
%autosetup -n %{name}-%{name}-%{version}
find src -type f -executable -exec chmod -x '{}' \;

%build
export CFLAGS="%optflags" CXXFLAGS="%optflags"
%make_build

# XXX: enable this once https://github.com/dburkart/check-sieve/pull/36 is merged
%check
make test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_bindir}
install check-sieve %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_mandir}/man1
gzip -9 ./docs/man1/check-sieve.1
install ./docs/man1/check-sieve.1.gz %{buildroot}%{_mandir}/man1

%files
%license COPYING
%doc README.md
%{_bindir}/check-sieve
%{_mandir}/*

%changelog
* Mon Jul 27 2020 Evan Klitzke <evan@eklitzke.org> - 0.6-2
- Enable "make test" checks

* Mon Jul 27 2020 Evan Klitzke <evan@eklitzke.org> - 0.6-1
- Bump for upstream version 0.6

* Mon Apr  1 2019 Evan Klitzke <evan@eklitzke.org> - 0.5-1
- Initial package.
