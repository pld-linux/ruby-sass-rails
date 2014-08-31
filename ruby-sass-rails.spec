%define		pkgname	sass-rails
Summary:	Sass adapter for the Rails asset pipeline
Name:		ruby-%{pkgname}
Version:	3.2.6
Release:	0.1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/gems/%{pkgname}-%{version}.gem
# Source0-md5:	b81ae64fa2d1c593d894cbeebbe4e017
URL:		http://github.com/rtomayko/%{pkgname}
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
Requires:	ruby-railties
Requires:	ruby-sass
Requires:	ruby-tilt
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sass adapter for the Rails asset pipeline.

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

rdoc --ri --op ri lib
rdoc --op rdoc lib
# rm -r ri/NOT_THIS_MODULE_RELATED_DIRS
rm ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_ridir},%{ruby_rdocdir}}

cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
install -d $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}
cp -a rdoc/* $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

install -d $RPM_BUILD_ROOT%{ruby_specdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README.markdown
%{ruby_vendorlibdir}/sass/rails
%{ruby_vendorlibdir}/sass/rails.rb
%{ruby_vendorlibdir}/sass-rails.rb
#/usr/share/ruby/vendor_ruby/rails/generators/sass/assets/assets_generator.rb
#/usr/share/ruby/vendor_ruby/rails/generators/sass/assets/templates/stylesheet.css.sass
#/usr/share/ruby/vendor_ruby/rails/generators/sass/scaffold/scaffold_generator.rb
#/usr/share/ruby/vendor_ruby/rails/generators/sass_scaffold.rb
#/usr/share/ruby/vendor_ruby/rails/generators/scss/assets/assets_generator.rb
#/usr/share/ruby/vendor_ruby/rails/generators/scss/assets/templates/stylesheet.css.scss
#/usr/share/ruby/vendor_ruby/rails/generators/scss/scaffold/scaffold_generator.rb
%{ruby_specdir}/%{pkgname}-%{version}.gemspec

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/Sass
%{ruby_ridir}/Scss
