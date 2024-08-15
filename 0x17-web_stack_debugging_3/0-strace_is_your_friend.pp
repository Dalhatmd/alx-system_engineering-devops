# Puppet manifest to fix an issue with apache2 server


exec { 'replace':
  command => "sed -i 's/phpp/php/g' '/var/www/html/wp-settings.php'",
  path    => ['/bin', '/usr/bin']
}
