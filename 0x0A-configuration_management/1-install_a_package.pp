#installs a package using pip
package { 'flask' :
    ensure   => '2.1.0',
    provider => 'pip3',
}
