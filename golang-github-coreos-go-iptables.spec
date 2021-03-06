#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : golang-github-coreos-go-iptables
Version  : fbb73372b87f6e89951c2b6b31470c2c9d5cfae3
Release  : 6
URL      : https://github.com/coreos/go-iptables/archive/fbb73372b87f6e89951c2b6b31470c2c9d5cfae3.tar.gz
Source0  : https://github.com/coreos/go-iptables/archive/fbb73372b87f6e89951c2b6b31470c2c9d5cfae3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : go
BuildRequires : iptables

%description
# go-iptables
[![Build Status](https://travis-ci.org/coreos/go-iptables.png?branch=master)](https://travis-ci.org/coreos/go-iptables)

%prep
%setup -q -n go-iptables-fbb73372b87f6e89951c2b6b31470c2c9d5cfae3

%build

%install
gopath="/usr/lib/golang"
library_path="github.com/coreos/go-iptables"
rm -rf %{buildroot}
install -d -p %{buildroot}${gopath}/src/${library_path}/
for file in $(find . -iname "*.go" -o -iname "*.h" -o -iname "*.c") ; do
     echo ${file}
     install -d -p %{buildroot}${gopath}/src/${library_path}/$(dirname $file)
     cp -pav $file %{buildroot}${gopath}/src/${library_path}/$file
done


%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/coreos/go-iptables/iptables/iptables.go
/usr/lib/golang/src/github.com/coreos/go-iptables/iptables/iptables_test.go
/usr/lib/golang/src/github.com/coreos/go-iptables/iptables/lock.go
